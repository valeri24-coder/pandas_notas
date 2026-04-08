from flask import Flask, render_template, request, redirect, session, send_file
from database import obtenerusuarios, insertar_estudiante, conectar
from dashprincipal import creartablero
import pandas as pd
import unicodedata
import io

app = Flask(__name__)
app.secret_key = "super_secret_key"

# crear dashboard
creartablero(app)

# evitar cache en paginas protegidas
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store,no-cache,must-revalidate,max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# FUNCIONES AUXILIARES
def quitar_acentos(texto):
    """Elimina tildes y caracteres especiales de un texto."""
    if pd.isna(texto):
        return texto
    texto = str(texto)
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def calculardesempeno(prom):
    """Retorna el nivel de desempeño según el promedio."""
    if prom >= 4.5:
        return "Excelente"
    elif prom >= 4:
        return "Bueno"
    elif prom >= 3:
        return "Regular"
    else:
        return "Bajo"


def estudiante_existe(nombre, carrera):
    """Retorna True si ya existe un estudiante con el mismo nombre y carrera en la BD."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM estudiantes WHERE nombre_estu = %s AND carrera = %s",
        (nombre, carrera)
    )
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] > 0


# LOGIN

@app.route("/", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        usuario  = obtenerusuarios(username)

        if usuario:
            if usuario["passworduser"] == password:
                session["username"] = usuario["username"]
                session["rol"]      = usuario["rolusu"]
                return redirect("/dashprincipal")
            else:
                error = "Contraseña incorrecta"
        else:
            error = "Usuario no existe"

    return render_template("login.html", error=error)


# DASHBOARD  (Punto 6: alerta de riesgo incluida)

@app.route("/dashprincipal")
def dashprinci():

    if "username" not in session:
        return redirect("/")

    # PUNTO 6: consultar estudiantes en riesgo para mostrar alerta directamente en el dashboard
    conn   = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT nombre_estu, carrera, promedio
           FROM estudiantes
           WHERE promedio < 3.0
           ORDER BY promedio ASC"""
    )
    filas = cursor.fetchall()
    conn.close()

    estudiantes_riesgo = [
        {"nombre": f[0], "carrera": f[1], "promedio": f[2]}
        for f in filas
    ]

    return render_template(
        "dashprinci.html",
        usuario=session["username"],
        estudiantes_riesgo=estudiantes_riesgo,
        total_riesgo=len(estudiantes_riesgo)
    )

# LOGOUT

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# REGISTRO INDIVIDUAL  (Punto 1: validar duplicados)

@app.route("/registro_estudiante", methods=["GET", "POST"])
def registro_estudiante():

    if "username" not in session:
        return redirect("/")

    error = None

    if request.method == "POST":

        nombre  = request.form["txtnombre"].strip().title()
        edad    = request.form["txtedad"]
        carrera = request.form["txtcarrera"].strip().title()
        nota1   = float(request.form["txtnota1"])
        nota2   = float(request.form["txtnota2"])
        nota3   = float(request.form["txtnota3"])

        # PUNTO 1: verificar duplicado antes de insertar
        if estudiante_existe(nombre, carrera):
            error = f"El estudiante '{nombre}' ya está registrado en la carrera '{carrera}'."
            return render_template("registro_estudiante.html", error=error)

        promedio  = round((nota1 + nota2 + nota3) / 3, 2)
        desempeno = calculardesempeno(promedio)
        insertar_estudiante(nombre, edad, carrera, nota1, nota2, nota3, promedio, desempeno)

        return redirect("/dashprincipal")

    return render_template("registro_estudiante.html", error=error)


# CARGA MASIVA  (Puntos 1, 2, 3, 4)

@app.route("/carga_masiva", methods=["GET", "POST"])
def carga_masiva():

    if "username" not in session:
        return redirect("/")

    if request.method == "POST":

        archivo = request.files["archivo"]

        if archivo:

            df = pd.read_excel(archivo)
            columnas_requeridas = ["Nombre", "Edad", "Carrera", "Nota1", "Nota2", "Nota3"]

            lista_rechazados = []
            insertados = 0
            duplicados = 0

            #  Detectar filas con datos faltantes 
            mask_faltantes = df[columnas_requeridas].isnull().any(axis=1)
            faltantes = df[mask_faltantes].copy()
            if not faltantes.empty:
                faltantes["Motivo_Rechazo"] = "Datos faltantes"
                lista_rechazados.append(faltantes)
            df = df[~mask_faltantes]

            #  Limpiar texto 
            for col in ["Nombre", "Carrera"]:
                df[col] = df[col].astype(str).str.strip()
                df[col] = df[col].apply(quitar_acentos)
                df[col] = df[col].str.title()

            #  Detectar edades negativas 
            mask_edad = df["Edad"] < 0
            edad_invalida = df[mask_edad].copy()
            if not edad_invalida.empty:
                edad_invalida["Motivo_Rechazo"] = "Edad negativa"
                lista_rechazados.append(edad_invalida)
            df = df[~mask_edad]

            #  Detectar notas fuera de rango 
            mask_notas = ~(
                df["Nota1"].between(0, 5) &
                df["Nota2"].between(0, 5) &
                df["Nota3"].between(0, 5)
            )
            notas_invalidas = df[mask_notas].copy()
            if not notas_invalidas.empty:
                notas_invalidas["Motivo_Rechazo"] = "Notas fuera del rango 0-5"
                lista_rechazados.append(notas_invalidas)
            df = df[~mask_notas]

            # Calcular promedio y desempeño
            df = df.copy()
            df["Promedio"]  = ((df["Nota1"] + df["Nota2"] + df["Nota3"]) / 3).round(2)
            df["Desempeno"] = df["Promedio"].apply(calculardesempeno)

            # Detectar duplicados dentro del mismo Excel
            mask_dup_excel = df.duplicated(subset=["Nombre", "Carrera"], keep="first")
            dup_excel = df[mask_dup_excel].copy()
            if not dup_excel.empty:
                dup_excel["Motivo_Rechazo"] = "Duplicado dentro del archivo Excel"
                lista_rechazados.append(dup_excel)
                duplicados += len(dup_excel)
            df = df[~mask_dup_excel]

            #Insertar en BD verificando duplicados contra la base ──
            conn   = conectar()
            cursor = conn.cursor()

            for _, row in df.iterrows():

                # PUNTO 1: verificar contra la BD antes de insertar
                cursor.execute(
                    "SELECT COUNT(*) FROM estudiantes WHERE nombre_estu = %s AND carrera = %s",
                    (row["Nombre"], row["Carrera"])
                )
                if cursor.fetchone()[0] > 0:
                    fila_dup = row.to_dict()
                    fila_dup["Motivo_Rechazo"] = "Ya existe en la base de datos"
                    lista_rechazados.append(pd.DataFrame([fila_dup]))
                    duplicados += 1
                    continue

                cursor.execute(
                    """INSERT INTO estudiantes
                       (nombre_estu, edad_estu, carrera, nota1, nota2, nota3, promedio, desempeno)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                    (row["Nombre"], row["Edad"], row["Carrera"],
                     row["Nota1"],  row["Nota2"], row["Nota3"],
                     row["Promedio"], row["Desempeno"])
                )
                insertados += 1

            conn.commit()
            conn.close()

            # ── Consolidar rechazados y guardar en sesión para descarga ──
            if lista_rechazados:
                df_rechazados    = pd.concat(lista_rechazados, ignore_index=True)
                total_rechazados = len(df_rechazados)
                session["rechazados"] = df_rechazados.astype(str).to_dict(orient="records")
            else:
                total_rechazados = 0
                session["rechazados"] = []

            # PUNTO 2: traer TODOS los estudiantes para mostrar en la tabla actualizada
            conn   = conectar()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT nombre_estu, edad_estu, carrera, nota1, nota2, nota3, promedio, desempeno
                   FROM estudiantes
                   ORDER BY nombre_estu"""
            )
            filas = cursor.fetchall()
            conn.close()

            todos = [
                {
                    "nombre": f[0], "edad": f[1], "carrera": f[2],
                    "nota1":  f[3], "nota2": f[4], "nota3":  f[5],
                    "promedio": f[6], "desempeno": f[7]
                }
                for f in filas
            ]

            # PUNTO 4: estadísticas del cargue
            stats = {
                "insertados": insertados,
                "rechazados": total_rechazados,
                "duplicados": duplicados
            }

            # PUNTOS 2 y 4: renderizar resultado con tabla completa y estadísticas
            return render_template(
                "resultado_carga.html",
                stats=stats,
                estudiantes=todos,
                hay_rechazados=(total_rechazados > 0)
            )

    return render_template("carga_masiva.html")

# DESCARGAR RECHAZADOS  (Punto 3)

@app.route("/descargar_rechazados")
def descargar_rechazados():

    if "username" not in session:
        return redirect("/")

    rechazados = session.get("rechazados", [])

    if not rechazados:
        return redirect("/dashprincipal")

    df_rechazados = pd.DataFrame(rechazados)

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df_rechazados.to_excel(writer, index=False, sheet_name="Rechazados")
    output.seek(0)

    return send_file(
        output,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name="registros_rechazados.xlsx"
    )

# RANKING  (Punto 5)

@app.route("/ranking")
def ranking():

    if "username" not in session:
        return redirect("/")

    conn   = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT nombre_estu, carrera, promedio
           FROM estudiantes
           ORDER BY promedio DESC
           LIMIT 10"""
    )
    filas = cursor.fetchall()
    conn.close()

    ranking_list = [
        {"posicion": i + 1, "nombre": f[0], "carrera": f[1], "promedio": f[2]}
        for i, f in enumerate(filas)
    ]

    return render_template("ranking.html", ranking=ranking_list)


if __name__ == "__main__":
    app.run(debug=True)
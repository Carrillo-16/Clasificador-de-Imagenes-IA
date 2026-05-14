import axios from "axios";
import { NombreModelo, ResultadoPrediccion } from "../tipos/prediccion";

const clienteApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL || (import.meta.env.PROD ? "/api" : "http://127.0.0.1:8000")
});

export async function enviarImagenParaPrediccion(
  imagenSeleccionada: File,
  nombreModelo: NombreModelo
): Promise<ResultadoPrediccion> {
  const datosFormulario = new FormData();
  datosFormulario.append("imagen", imagenSeleccionada);
  datosFormulario.append("nombre_modelo", nombreModelo);
  datosFormulario.append("nombre_usuario", "Estudiante");
  datosFormulario.append("correo_usuario", "estudiante@universidad.com");

  const respuesta = await clienteApi.post<ResultadoPrediccion>("/predecir", datosFormulario, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });

  return respuesta.data;
}

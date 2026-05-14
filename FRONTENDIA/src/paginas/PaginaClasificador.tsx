import { useState } from "react";

import { CargadorImagen } from "../componentes/CargadorImagen";
import { ResultadoPrediccion } from "../componentes/ResultadoPrediccion";
import { SelectorModelo } from "../componentes/SelectorModelo";
import { enviarImagenParaPrediccion } from "../servicios/servicioPrediccion";
import { NombreModelo, ResultadoPrediccion as TipoResultadoPrediccion } from "../tipos/prediccion";

export function PaginaClasificador() {
  const [imagenSeleccionada, cambiarImagenSeleccionada] = useState<File | null>(null);
  const [nombreModelo, cambiarNombreModelo] = useState<NombreModelo>("MobileNetV2");
  const [resultadosPrediccion, cambiarResultadosPrediccion] = useState<TipoResultadoPrediccion[]>([]);
  const [vistaPrevia, cambiarVistaPrevia] = useState("");
  const [cargando, cambiarCargando] = useState(false);
  const [mensajeError, cambiarMensajeError] = useState("");

  async function manejarPrediccion(compararModelos: boolean) {
    if (!imagenSeleccionada) {
      cambiarMensajeError("Selecciona una imagen antes de predecir.");
      return;
    }

    cambiarCargando(true);
    cambiarMensajeError("");
    cambiarResultadosPrediccion([]);

    try {
      if (compararModelos) {
        const resultados: TipoResultadoPrediccion[] = [];

        const resultadoMobileNet = await enviarImagenParaPrediccion(imagenSeleccionada, "MobileNetV2");
        resultados.push(resultadoMobileNet);
        cambiarResultadosPrediccion([...resultados]);

        const resultadoResNet = await enviarImagenParaPrediccion(imagenSeleccionada, "ResNet50");
        resultados.push(resultadoResNet);

        cambiarResultadosPrediccion(resultados);
      } else {
        const resultado = await enviarImagenParaPrediccion(imagenSeleccionada, nombreModelo);
        cambiarResultadosPrediccion([resultado]);
      }
    } catch {
      cambiarMensajeError("No se pudo realizar la prediccion. Verifica que el backend este ejecutandose.");
    } finally {
      cambiarCargando(false);
    }
  }

  return (
    <main
      style={{
        minHeight: "100vh",
        boxSizing: "border-box",
        padding: 24,
        background: "#eef2f6",
        color: "#17202a",
        fontFamily: "Arial, sans-serif"
      }}
    >
      <section
        style={{
          maxWidth: 760,
          margin: "0 auto",
          display: "grid",
          gap: 20,
          padding: 24,
          borderRadius: 8,
          background: "#ffffff",
          border: "1px solid #d7dce3"
        }}
      >
        <div style={{ display: "grid", gap: 6 }}>
          <h1 style={{ margin: 0, fontSize: 30 }}>Clasificador de Imagenes</h1>
          <p style={{ margin: 0, color: "#4a5564" }}>Modelos ImageNet preentrenados: MobileNetV2 y ResNet50</p>
        </div>

        <SelectorModelo nombreModelo={nombreModelo} cambiarNombreModelo={cambiarNombreModelo} />

        <CargadorImagen
          cambiarImagenSeleccionada={cambiarImagenSeleccionada}
          vistaPrevia={vistaPrevia}
          cambiarVistaPrevia={cambiarVistaPrevia}
        />

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
          <button
            type="button"
            onClick={() => manejarPrediccion(false)}
            disabled={cargando}
            style={{
              padding: 14,
              borderRadius: 6,
              border: "none",
              background: cargando ? "#7b8794" : "#2563eb",
              color: "#ffffff",
              fontSize: 16,
              fontWeight: 700,
              cursor: cargando ? "not-allowed" : "pointer"
            }}
          >
            {cargando ? "Prediciendo..." : "Predecir"}
          </button>

          <button
            type="button"
            onClick={() => manejarPrediccion(true)}
            disabled={cargando}
            style={{
              padding: 14,
              borderRadius: 6,
              border: "1px solid #2563eb",
              background: "#ffffff",
              color: "#2563eb",
              fontSize: 16,
              fontWeight: 700,
              cursor: cargando ? "not-allowed" : "pointer"
            }}
          >
            Comparar modelos
          </button>
        </div>

        {mensajeError && (
          <p style={{ margin: 0, color: "#b42318", fontWeight: 600 }}>{mensajeError}</p>
        )}

        <ResultadoPrediccion resultadosPrediccion={resultadosPrediccion} />
      </section>
    </main>
  );
}

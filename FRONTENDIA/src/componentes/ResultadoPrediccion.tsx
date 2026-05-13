import { ResultadoPrediccion as TipoResultadoPrediccion } from "../tipos/prediccion";

interface PropiedadesResultadoPrediccion {
  resultadosPrediccion: TipoResultadoPrediccion[];
}

export function ResultadoPrediccion({ resultadosPrediccion }: PropiedadesResultadoPrediccion) {
  if (resultadosPrediccion.length === 0) {
    return null;
  }

  return (
    <div style={{ display: "grid", gap: 16 }}>
      {resultadosPrediccion.map((resultadoPrediccion) => (
        <section
          key={resultadoPrediccion.modelo}
          style={{
            display: "grid",
            gap: 12,
            padding: 16,
            borderRadius: 6,
            border: "1px solid #b8c0cc",
            background: "#f7fafc"
          }}
        >
          <h2 style={{ margin: 0, fontSize: 22 }}>{resultadoPrediccion.modelo}</h2>
          <ol style={{ margin: 0, paddingLeft: 22, display: "grid", gap: 8 }}>
            {resultadoPrediccion.predicciones.map((prediccion) => (
              <li key={`${resultadoPrediccion.modelo}-${prediccion.clase}`}>
                <span style={{ fontWeight: 700 }}>{prediccion.clase}</span>
                <span style={{ color: "#4a5564" }}> - {prediccion.confianza}</span>
              </li>
            ))}
          </ol>
        </section>
      ))}
    </div>
  );
}

import { NombreModelo } from "../tipos/prediccion";

interface PropiedadesSelectorModelo {
  nombreModelo: NombreModelo;
  cambiarNombreModelo: (nombreModelo: NombreModelo) => void;
}

export function SelectorModelo({ nombreModelo, cambiarNombreModelo }: PropiedadesSelectorModelo) {
  return (
    <label style={{ display: "grid", gap: 8, fontWeight: 600 }}>
      Modelo preentrenado
      <select
        value={nombreModelo}
        onChange={(evento) => cambiarNombreModelo(evento.target.value as NombreModelo)}
        style={{
          padding: 12,
          borderRadius: 6,
          border: "1px solid #b8c0cc",
          fontSize: 16
        }}
      >
        <option value="MobileNetV2">MobileNetV2</option>
        <option value="ResNet50">ResNet50</option>
      </select>
    </label>
  );
}

import { ChangeEvent } from "react";

interface PropiedadesCargadorImagen {
  cambiarImagenSeleccionada: (imagen: File | null) => void;
  vistaPrevia: string;
  cambiarVistaPrevia: (vistaPrevia: string) => void;
}

export function CargadorImagen({
  cambiarImagenSeleccionada,
  vistaPrevia,
  cambiarVistaPrevia
}: PropiedadesCargadorImagen) {
  function manejarCambioImagen(evento: ChangeEvent<HTMLInputElement>) {
    const archivo = evento.target.files?.[0] ?? null;
    cambiarImagenSeleccionada(archivo);

    if (archivo) {
      cambiarVistaPrevia(URL.createObjectURL(archivo));
    } else {
      cambiarVistaPrevia("");
    }
  }

  return (
    <div style={{ display: "grid", gap: 12 }}>
      <label style={{ display: "grid", gap: 8, fontWeight: 600 }}>
        Imagen
        <input
          type="file"
          accept="image/*"
          onChange={manejarCambioImagen}
          style={{
            padding: 12,
            borderRadius: 6,
            border: "1px solid #b8c0cc",
            fontSize: 16
          }}
        />
      </label>

      {vistaPrevia && (
        <img
          src={vistaPrevia}
          alt="Vista previa"
          style={{
            width: "100%",
            maxHeight: 280,
            objectFit: "contain",
            borderRadius: 6,
            border: "1px solid #d7dce3",
            background: "#ffffff"
          }}
        />
      )}
    </div>
  );
}

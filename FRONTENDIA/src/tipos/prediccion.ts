export interface ResultadoPrediccion {
  modelo: string;
  predicciones: PrediccionImagenNet[];
}

export interface PrediccionImagenNet {
  clase: string;
  confianza: string;
}

export type NombreModelo = "MobileNetV2" | "ResNet50";

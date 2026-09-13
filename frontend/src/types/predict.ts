/** One entry in the top-k predictions list */
export interface TopKItem {
  class_label: string;
  confidence: number; // 0.0 – 1.0
}

/** Full response from POST /predict */
export interface PredictResult {
  class_label: string;
  confidence: number; // 0.0 – 1.0
  is_healthy: boolean;
  description: string;
  treatment: string[];
  top_k: TopKItem[];
}

/** Discriminated union for the upload/diagnose lifecycle */
export type UploadState =
  | { status: 'idle' }
  | { status: 'previewing'; file: File; previewUrl: string }
  | { status: 'loading'; file: File; previewUrl: string }
  | { status: 'result'; file: File; previewUrl: string; result: PredictResult }
  | { status: 'error'; file: File | null; previewUrl: string | null; message: string };

/** Return type of apiClient.predict() */
export type ApiResult =
  | { ok: true; data: PredictResult }
  | { ok: false; error: string };

/** Upload constants */
export const MAX_UPLOAD_BYTES = 10 * 1024 * 1024; // 10 MB
export const ALLOWED_TYPES = new Set(['image/jpeg', 'image/png', 'image/webp']);
export const REQUEST_TIMEOUT_MS = 30_000; // 30 seconds
export const LOW_CONF_THRESHOLD = 0.4;

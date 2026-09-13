import type { ApiResult, PredictResult } from '../types/predict';
import { REQUEST_TIMEOUT_MS } from '../types/predict';

export async function predict(file: File): Promise<ApiResult> {
  const ctrl = new AbortController();
  const timerId = setTimeout(() => ctrl.abort(), REQUEST_TIMEOUT_MS);
  const formData = new FormData();
  formData.append('file', file);

  try {
    const res = await fetch('/predict', {
      method: 'POST',
      body: formData,
      signal: ctrl.signal,
    });
    clearTimeout(timerId);

    if (res.ok) {
      const data = (await res.json()) as PredictResult;
      return { ok: true, data };
    }

    if (res.status >= 400 && res.status < 500) {
      let detail = 'An error occurred.';
      try {
        const body = (await res.json()) as { detail?: string };
        detail = body.detail ?? detail;
      } catch (_) {
        // ignore JSON parse errors
      }
      return { ok: false, error: detail };
    }

    return {
      ok: false,
      error: 'Something went wrong on our end. Please try again.',
    };
  } catch (err) {
    clearTimeout(timerId);
    if (err instanceof Error && err.name === 'AbortError') {
      return { ok: false, error: 'The request timed out. Please try again.' };
    }
    return {
      ok: false,
      error: 'Unable to reach the server. Check your connection and try again.',
    };
  }
}

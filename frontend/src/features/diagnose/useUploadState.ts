import { useReducer, useEffect, Dispatch } from 'react';
import type { UploadState, PredictResult } from '../../types/predict';
import { ALLOWED_TYPES, MAX_UPLOAD_BYTES } from '../../types/predict';

export type Action =
  | { type: 'SELECT_FILE'; file: File; previewUrl: string }
  | { type: 'CLEAR' }
  | { type: 'SUBMIT' }
  | { type: 'SUCCESS'; result: PredictResult }
  | { type: 'API_ERROR'; message: string }
  | { type: 'VALIDATION_ERROR'; message: string };

const initialState: UploadState = { status: 'idle' };

function reducer(state: UploadState, action: Action): UploadState {
  switch (action.type) {
    case 'SELECT_FILE': {
      if (state.status === 'loading') return state;
      return { status: 'previewing', file: action.file, previewUrl: action.previewUrl };
    }
    case 'CLEAR': {
      if (state.status === 'loading') return state;
      return { status: 'idle' };
    }
    case 'SUBMIT': {
      if (state.status !== 'previewing') return state;
      return { status: 'loading', file: state.file, previewUrl: state.previewUrl };
    }
    case 'SUCCESS': {
      if (state.status !== 'loading') return state;
      return {
        status: 'result',
        file: state.file,
        previewUrl: state.previewUrl,
        result: action.result,
      };
    }
    case 'API_ERROR': {
      if (state.status !== 'loading') return state;
      return {
        status: 'error',
        file: state.file,
        previewUrl: state.previewUrl,
        message: action.message,
      };
    }
    case 'VALIDATION_ERROR': {
      return { status: 'error', file: null, previewUrl: null, message: action.message };
    }
    default:
      return state;
  }
}

export interface UseUploadStateReturn {
  state: UploadState;
  dispatch: Dispatch<Action>;
}

export function useUploadState(): UseUploadStateReturn {
  const [state, dispatch] = useReducer(reducer, initialState);

  // Revoke object URL when no longer needed to prevent memory leaks
  useEffect(() => {
    return () => {
      if (
        (state.status === 'previewing' ||
          state.status === 'loading' ||
          state.status === 'result') &&
        state.previewUrl
      ) {
        URL.revokeObjectURL(state.previewUrl);
      }
    };
  }, [state]);

  return { state, dispatch };
}

/** Pure reducer export for testing without React hooks */
export { reducer as uploadReducer, initialState };

/**
 * Validate a file against allowed types and size limits.
 * Returns an error message string or null if valid.
 */
export function validateFile(file: File): string | null {
  if (!ALLOWED_TYPES.has(file.type)) {
    return 'Unsupported file type. Please upload a JPEG, PNG, or WebP image.';
  }
  if (file.size > MAX_UPLOAD_BYTES) {
    const mb = (file.size / 1024 / 1024).toFixed(1);
    return `File is too large (${mb} MB). Max 10 MB.`;
  }
  return null;
}

import { useRef, useEffect, DragEvent, KeyboardEvent } from 'react';
import { predict } from '../../api/apiClient';
import { LOW_CONF_THRESHOLD } from '../../types/predict';
import { useUploadState, validateFile } from './useUploadState';

export default function DiagnoseTool() {
  const { state, dispatch } = useUploadState();
  const fileInputRef = useRef<HTMLInputElement>(null);
  const resultsSectionRef = useRef<HTMLElement>(null);
  const isDragging = useRef(false);

  // Scroll to results on success
  useEffect(() => {
    if (state.status === 'result') {
      resultsSectionRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }, [state.status]);

  function handleFile(file: File) {
    const error = validateFile(file);
    if (error) {
      dispatch({ type: 'VALIDATION_ERROR', message: error });
      return;
    }
    const previewUrl = URL.createObjectURL(file);
    dispatch({ type: 'SELECT_FILE', file, previewUrl });
  }

  function handleDragEnter(e: DragEvent<HTMLDivElement>) {
    e.preventDefault();
    isDragging.current = true;
    e.currentTarget.classList.add('drag-over');
  }
  function handleDragOver(e: DragEvent<HTMLDivElement>) {
    e.preventDefault();
    if (e.dataTransfer) e.dataTransfer.dropEffect = 'copy';
    e.currentTarget.classList.add('drag-over');
  }
  function handleDragLeave(e: DragEvent<HTMLDivElement>) {
    if (!e.currentTarget.contains(e.relatedTarget as Node)) {
      e.currentTarget.classList.remove('drag-over');
      isDragging.current = false;
    }
  }
  function handleDrop(e: DragEvent<HTMLDivElement>) {
    e.preventDefault();
    e.currentTarget.classList.remove('drag-over');
    isDragging.current = false;
    const file = e.dataTransfer?.files?.[0];
    if (file) handleFile(file);
  }
  function handleKeyDown(e: KeyboardEvent<HTMLDivElement>) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      fileInputRef.current?.click();
    }
  }
  function handleInputChange() {
    const file = fileInputRef.current?.files?.[0];
    if (file) {
      handleFile(file);
      if (fileInputRef.current) fileInputRef.current.value = '';
    }
  }

  async function handleAnalyse() {
    if (state.status !== 'previewing') return;
    const { file } = state;
    dispatch({ type: 'SUBMIT' });
    const result = await predict(file);
    if (result.ok) {
      dispatch({ type: 'SUCCESS', result: result.data });
    } else {
      dispatch({ type: 'API_ERROR', message: result.error });
    }
  }

  const isDisabled = state.status === 'idle' || state.status === 'loading';
  const showPreview =
    state.status === 'previewing' ||
    state.status === 'loading' ||
    state.status === 'result';
  const previewUrl =
    state.status === 'previewing' || state.status === 'loading' || state.status === 'result'
      ? state.previewUrl
      : null;

  return (
    <div className="container diagnose-container">
      {/* Upload Panel */}
      <div className="upload-panel">
        <div
          id="upload-zone"
          className="upload-zone"
          role="button"
          tabIndex={0}
          aria-label="Upload zone. Drag and drop a leaf image, or press Enter to browse."
          aria-describedby="upload-hint"
          onDragEnter={handleDragEnter}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
          onKeyDown={handleKeyDown}
          onClick={() => fileInputRef.current?.click()}
        >
          <input
            ref={fileInputRef}
            type="file"
            id="file-input"
            accept="image/jpeg,image/png,image/webp"
            tabIndex={-1}
            style={{ position: 'absolute', inset: 0, opacity: 0, width: '100%', height: '100%', cursor: 'pointer', zIndex: 1 }}
            onChange={handleInputChange}
            onClick={e => e.stopPropagation()}
          />

          {!showPreview && (
            <div className="upload-prompt">
              <div className="upload-icon-wrap">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/>
                  <polyline points="17 8 12 3 7 8"/>
                  <line x1="12" y1="3" x2="12" y2="15"/>
                </svg>
              </div>
              <p className="upload-title">Drop your leaf photo here</p>
              <p className="upload-subtitle">or <span className="upload-link">click to browse files</span></p>
              <p id="upload-hint" className="upload-hint">JPEG · PNG · WebP · Max 10 MB</p>
            </div>
          )}

          {showPreview && previewUrl && (
            <div className="image-preview-container">
              <img
                className="image-preview"
                src={previewUrl}
                alt="Preview of uploaded leaf"
              />
              <button
                type="button"
                className="clear-btn"
                aria-label="Remove image"
                onClick={e => { e.stopPropagation(); dispatch({ type: 'CLEAR' }); }}
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                  <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
                </svg>
                Remove
              </button>
            </div>
          )}
        </div>

        <button
          type="button"
          className="btn btn-primary btn-analyse"
          disabled={isDisabled}
          aria-disabled={isDisabled ? 'true' : 'false'}
          onClick={handleAnalyse}
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
          </svg>
          Analyse Plant
        </button>

        <div className="tips-box">
          <h4 className="tips-title">📋 Tips for best results</h4>
          <ul className="tips-list">
            <li>Use a clear, close-up photo of a single leaf</li>
            <li>Ensure good lighting with no harsh shadows</li>
            <li>Keep the leaf in focus and fill the frame</li>
            <li>Avoid blurry or dark images</li>
          </ul>
        </div>
      </div>

      {/* Results Panel */}
      <div className="results-panel">
        {/* Error region */}
        {state.status === 'error' && (
          <div className="error-region" role="alert" aria-live="assertive">
            <span>⚠️  {state.message}</span>
          </div>
        )}

        {/* Loading */}
        {state.status === 'loading' && (
          <div className="loading-indicator" role="status">
            <div className="spinner-wrap"><div className="spinner"></div></div>
            <p className="loading-text">LeafLens AI is analysing your plant…</p>
            <p className="loading-sub">This may take a few seconds</p>
          </div>
        )}

        {/* Idle placeholder */}
        {state.status === 'idle' && (
          <div className="idle-placeholder">
            <div className="idle-icon">🔬</div>
            <h3 className="idle-title">Ready to Diagnose</h3>
            <p className="idle-desc">Upload a leaf photo on the left and click "Analyse Plant" to get your LeafLens AI diagnosis.</p>
          </div>
        )}

        {/* Results */}
        {state.status === 'result' && (
          <ResultsSection result={state.result} onReset={() => dispatch({ type: 'CLEAR' })} sectionRef={resultsSectionRef} />
        )}
      </div>
    </div>
  );
}

/* -------------------------------------------------------------------------- */

import type { PredictResult } from '../../types/predict';
import { RefObject } from 'react';

interface ResultsSectionProps {
  result: PredictResult;
  onReset: () => void;
  sectionRef: RefObject<HTMLElement>;
}

function ResultsSection({ result, onReset, sectionRef }: ResultsSectionProps) {
  const pct = Math.round(result.confidence * 100);
  const showWarning = result.confidence < LOW_CONF_THRESHOLD;
  const confBarRef = useRef<HTMLDivElement>(null);
  const topkListRef = useRef<HTMLUListElement>(null);

  // Animate bars on mount
  useEffect(() => {
    requestAnimationFrame(() =>
      requestAnimationFrame(() => {
        if (confBarRef.current) confBarRef.current.style.width = `${pct}%`;
        topkListRef.current?.querySelectorAll<HTMLElement>('.topk-bar').forEach(bar => {
          const p = bar.dataset.pct;
          if (p) bar.style.width = `${p}%`;
        });
      })
    );
  }, [pct]);

  return (
    <section className="results-section" aria-labelledby="results-heading" ref={sectionRef}>
      <h2 className="results-heading" id="results-heading">Diagnosis Result</h2>

      {showWarning && (
        <div className="warning-banner" role="alert">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/>
            <line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>
          </svg>
          <span>Low confidence — this may not be a clear plant leaf photo. For best results, upload a close-up of a single leaf.</span>
        </div>
      )}

      <div className={`disease-card ${result.is_healthy ? 'is-healthy' : 'is-diseased'}`}>
        <div className="card-header">
          <div className="card-label-row">
            <h3 className="card-label">{result.class_label}</h3>
            <span className={`health-badge ${result.is_healthy ? 'badge-healthy' : 'badge-diseased'}`}>
              {result.is_healthy ? '✓ Healthy' : '⚠ Disease Detected'}
            </span>
          </div>
          <div className="confidence-row">
            <span className="confidence-label">Confidence</span>
            <span className="confidence-value">{pct}%</span>
          </div>
          <div
            className="confidence-bar-track"
            role="progressbar"
            aria-valuemin={0}
            aria-valuemax={100}
            aria-valuenow={pct}
          >
            <div ref={confBarRef} className="confidence-bar" style={{ width: '0%' }}></div>
          </div>
        </div>

        {result.description && (
          <div className="card-section">
            <h4 className="card-section-title">About this condition</h4>
            <p className="card-description">{result.description}</p>
          </div>
        )}

        {!result.is_healthy && result.treatment && result.treatment.length > 0 && (
          <div className="card-section">
            <h4 className="card-section-title">Treatment &amp; Management</h4>
            <ul className="treatment-list">
              {result.treatment.map((t, i) => <li key={i}>{t}</li>)}
            </ul>
          </div>
        )}
      </div>

      <div className="topk-container">
        <h3 className="topk-heading">Top 3 Predictions</h3>
        <ul className="topk-list" ref={topkListRef}>
          {(result.top_k || []).map((item, i) => {
            const p = Math.round(item.confidence * 100);
            return (
              <li key={i} className="topk-item">
                <span className="topk-rank">#{i + 1}</span>
                <div className="topk-info">
                  <div className="topk-label">{item.class_label}</div>
                  <div className="topk-bar-track">
                    <div className="topk-bar" style={{ width: '0%' }} data-pct={p}></div>
                  </div>
                </div>
                <span className="topk-pct">{p}%</span>
              </li>
            );
          })}
        </ul>
      </div>

      <button type="button" className="btn btn-outline btn-full" onClick={onReset}>
        ↺ &nbsp;Diagnose Another Plant
      </button>
    </section>
  );
}

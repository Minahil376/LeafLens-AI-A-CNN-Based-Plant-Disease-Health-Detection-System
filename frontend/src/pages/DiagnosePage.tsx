import { useEffect } from 'react';
import DiagnoseTool from '../features/diagnose/DiagnoseTool';

export default function DiagnosePage() {
  useEffect(() => {
    document.title = 'Diagnose — LeafLens AI';
  }, []);

  return (
    <>
      {/* PAGE HEADER */}
      <div className="page-header">
        <div className="container">
          <span className="section-tag">AI Diagnosis</span>
          <h1 className="page-title">Plant Disease Diagnosis</h1>
          <p className="page-subtitle">Upload a clear photo of a plant leaf to get an instant LeafLens AI diagnosis</p>
        </div>
      </div>

      {/* DIAGNOSE TOOL */}
      <main className="diagnose-main">
        <DiagnoseTool />
      </main>
    </>
  );
}

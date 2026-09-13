import { useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function AboutPage() {
  useEffect(() => {
    document.title = 'About — LeafLens AI';
  }, []);

  return (
    <>
      {/* PAGE HEADER */}
      <div className="page-header">
        <div className="container">
          <span className="section-tag">About</span>
          <h1 className="page-title">About LeafLens AI</h1>
          <p className="page-subtitle">Learn how our AI model works and what it can do for your plants</p>
        </div>
      </div>

      <main className="about-main">
        <div className="container">

          {/* Mission */}
          <section className="about-section">
            <div className="about-grid">
              <div className="about-text">
                <span className="section-tag">Our Mission</span>
                <h2 className="about-title">Empowering Farmers &amp; Gardeners with AI</h2>
                <p>LeafLens AI brings cutting-edge deep learning technology to anyone who grows plants — from backyard gardeners to professional farmers. Early detection of plant diseases can save entire crops and reduce the need for pesticides.</p>
                <p>Our model was trained on the PlantVillage dataset, one of the largest publicly available plant disease image datasets, covering 38 plant-disease combinations across 14 crop species.</p>
              </div>
              <div className="about-visual">
                <div className="about-icon-card">
                  <span>🌱</span>
                  <span>🔬</span>
                  <span>💡</span>
                </div>
              </div>
            </div>
          </section>

          {/* Model Info */}
          <section className="about-section">
            <div className="section-header">
              <span className="section-tag">Technology</span>
              <h2 className="section-title">The Model Behind LeafLens AI</h2>
            </div>
            <div className="tech-grid">
              <div className="tech-card">
                <div className="tech-icon">🧠</div>
                <h3>ResNet50 Architecture</h3>
                <p>Built on the ResNet50 deep residual network, fine-tuned specifically for plant disease classification. ResNet50 is renowned for its accuracy on image classification tasks.</p>
              </div>
              <div className="tech-card">
                <div className="tech-icon">📊</div>
                <h3>PlantVillage Dataset</h3>
                <p>Trained on thousands of images from the PlantVillage dataset, covering 38 distinct plant-disease combinations across 14 major crop species.</p>
              </div>
              <div className="tech-card">
                <div className="tech-icon">⚡</div>
                <h3>Fast Inference</h3>
                <p>Powered by TensorFlow and FastAPI, LeafLens AI delivers predictions in seconds, even on standard CPU hardware — no GPU required.</p>
              </div>
              <div className="tech-card">
                <div className="tech-icon">🎯</div>
                <h3>38 Disease Classes</h3>
                <p>LeafLens AI classifies images into 38 categories including both healthy and diseased states, providing confidence scores for each prediction.</p>
              </div>
            </div>
          </section>

          {/* Diseases Table */}
          <section className="about-section">
            <div className="section-header">
              <span className="section-tag">Coverage</span>
              <h2 className="section-title">Diseases LeafLens AI Detects</h2>
              <p className="section-subtitle">LeafLens AI can identify the following plant conditions</p>
            </div>
            <div className="disease-table-wrap">
              <table className="disease-table">
                <thead>
                  <tr>
                    <th>Plant</th>
                    <th>Conditions Detected</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>🍎 Apple</td><td>Apple Scab, Black Rot, Cedar Apple Rust, Healthy</td></tr>
                  <tr><td>🫐 Blueberry</td><td>Healthy</td></tr>
                  <tr><td>🍒 Cherry</td><td>Powdery Mildew, Healthy</td></tr>
                  <tr><td>🌽 Corn</td><td>Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy</td></tr>
                  <tr><td>🍇 Grape</td><td>Black Rot, Esca (Black Measles), Leaf Blight, Healthy</td></tr>
                  <tr><td>🍊 Orange</td><td>Huanglongbing (Citrus Greening)</td></tr>
                  <tr><td>🍑 Peach</td><td>Bacterial Spot, Healthy</td></tr>
                  <tr><td>🫑 Bell Pepper</td><td>Bacterial Spot, Healthy</td></tr>
                  <tr><td>🥔 Potato</td><td>Early Blight, Late Blight, Healthy</td></tr>
                  <tr><td>🫐 Raspberry</td><td>Healthy</td></tr>
                  <tr><td>🌱 Soybean</td><td>Healthy</td></tr>
                  <tr><td>🥒 Squash</td><td>Powdery Mildew</td></tr>
                  <tr><td>🍓 Strawberry</td><td>Leaf Scorch, Healthy</td></tr>
                  <tr><td>🍅 Tomato</td><td>Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy</td></tr>
                </tbody>
              </table>
            </div>
          </section>

          {/* Limitations */}
          <section className="about-section">
            <div className="limitations-card">
              <h3 className="limitations-title">⚠️ Important Limitations</h3>
              <ul className="limitations-list">
                <li>LeafLens AI only recognises the 38 classes it was trained on — other plant species or diseases may produce incorrect results.</li>
                <li>Image quality matters significantly. Blurry, dark, or partial leaf images reduce accuracy.</li>
                <li>This tool is intended as a first-pass diagnostic aid, not a replacement for professional agronomist advice.</li>
                <li>Low confidence scores (below 40%) indicate the model is uncertain — treat those results with caution.</li>
              </ul>
            </div>
          </section>

          {/* CTA */}
          <section className="about-section about-cta">
            <div className="cta-card">
              <div className="cta-content">
                <h2 className="cta-title">Try LeafLens AI Now</h2>
                <p className="cta-subtitle">Free, instant, and no account required.</p>
                <Link to="/diagnose" className="btn btn-white btn-lg">
                  Start Diagnosing
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </Link>
              </div>
              <div className="cta-decoration">🌿</div>
            </div>
          </section>

        </div>
      </main>
    </>
  );
}

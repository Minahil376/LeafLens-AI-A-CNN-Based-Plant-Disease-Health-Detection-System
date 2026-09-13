import { useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function HomePage() {
  useEffect(() => {
    document.title = 'LeafLens AI — Plant Disease Detection';
  }, []);

  return (
    <>
      {/* HERO */}
      <section className="hero">
        <div className="hero-bg">
          <div className="hero-shape hero-shape-1"></div>
          <div className="hero-shape hero-shape-2"></div>
          <div className="hero-shape hero-shape-3"></div>
        </div>
        <div className="container hero-container">
          <div className="hero-content">
            <div className="hero-badge">
              <span className="badge-dot"></span>
              AI-Powered Plant Diagnostics
            </div>
            <h1 className="hero-title">
              Detect Plant Diseases<br />
              <span className="hero-title-accent">Instantly with AI</span>
            </h1>
            <p className="hero-subtitle">
              Upload a photo of any plant leaf and get an accurate disease diagnosis in seconds.
              Powered by ResNet50 deep learning trained on 38 plant disease classes.
            </p>
            <div className="hero-actions">
              <Link to="/diagnose" className="btn btn-primary btn-lg">
                <span>Diagnose Your Plant</span>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </Link>
              <Link to="/about" className="btn btn-outline btn-lg">Learn More</Link>
            </div>
            <div className="hero-stats">
              <div className="stat">
                <span className="stat-number">38</span>
                <span className="stat-label">Disease Classes</span>
              </div>
              <div className="stat-divider"></div>
              <div className="stat">
                <span className="stat-number">14</span>
                <span className="stat-label">Plant Species</span>
              </div>
              <div className="stat-divider"></div>
              <div className="stat">
                <span className="stat-number">AI</span>
                <span className="stat-label">Powered</span>
              </div>
            </div>
          </div>
          <div className="hero-visual">
            <div className="hero-card">
              <div className="hero-card-img">🌱</div>
              <div className="hero-card-result">
                <div className="hero-card-badge healthy">✓ Healthy</div>
                <div className="hero-card-label">Tomato Leaf</div>
                <div className="hero-card-confidence"><span>Confidence</span><span className="hero-card-pct">97%</span></div>
                <div className="hero-card-bar"><div className="hero-card-fill" style={{ width: '97%' }}></div></div>
              </div>
            </div>
            <div className="hero-card hero-card-2">
              <div className="hero-card-img">🍃</div>
              <div className="hero-card-result">
                <div className="hero-card-badge diseased">⚠ Diseased</div>
                <div className="hero-card-label">Apple Scab</div>
                <div className="hero-card-confidence"><span>Confidence</span><span className="hero-card-pct">91%</span></div>
                <div className="hero-card-bar"><div className="hero-card-fill diseased-fill" style={{ width: '91%' }}></div></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* HOW IT WORKS */}
      <section className="section how-it-works">
        <div className="container">
          <div className="section-header">
            <span className="section-tag">Simple Process</span>
            <h2 className="section-title">How It Works</h2>
            <p className="section-subtitle">Get your plant diagnosis in three easy steps</p>
          </div>
          <div className="steps-grid">
            <div className="step-card">
              <div className="step-number">01</div>
              <div className="step-icon">📸</div>
              <h3 className="step-title">Upload a Photo</h3>
              <p className="step-desc">Take a clear close-up photo of the plant leaf you want to diagnose. JPEG, PNG, or WebP supported.</p>
            </div>
            <div className="step-arrow">→</div>
            <div className="step-card">
              <div className="step-number">02</div>
              <div className="step-icon">🤖</div>
              <h3 className="step-title">AI Analysis</h3>
              <p className="step-desc">LeafLens AI's ResNet50 model analyses the image and identifies potential diseases with high accuracy.</p>
            </div>
            <div className="step-arrow">→</div>
            <div className="step-card">
              <div className="step-number">03</div>
              <div className="step-icon">💊</div>
              <h3 className="step-title">Get Results</h3>
              <p className="step-desc">Receive a detailed diagnosis with confidence score, disease description, and treatment recommendations.</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section cta-section">
        <div className="container">
          <div className="cta-card">
            <div className="cta-content">
              <h2 className="cta-title">Ready to diagnose your plant?</h2>
              <p className="cta-subtitle">LeafLens AI is free, instant, and accurate. No sign-up required.</p>
              <Link to="/diagnose" className="btn btn-white btn-lg">
                <span>Start Diagnosing Now</span>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </Link>
            </div>
            <div className="cta-decoration">🌿</div>
          </div>
        </div>
      </section>

      {/* SUPPORTED PLANTS */}
      <section className="section plants-section">
        <div className="container">
          <div className="section-header">
            <span className="section-tag">Coverage</span>
            <h2 className="section-title">Supported Plants</h2>
            <p className="section-subtitle">LeafLens AI can diagnose diseases in these plant species</p>
          </div>
          <div className="plants-grid">
            {['🍎 Apple','🫐 Blueberry','🍒 Cherry','🌽 Corn','🍇 Grape','🍊 Orange',
              '🍑 Peach','🫑 Bell Pepper','🥔 Potato','🫐 Raspberry','🌱 Soybean',
              '🥒 Squash','🍓 Strawberry','🍅 Tomato'].map(plant => (
              <div key={plant} className="plant-chip">{plant}</div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}

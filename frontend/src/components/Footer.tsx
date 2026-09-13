import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <footer className="footer">
      <div className="container footer-container">
        <div className="footer-brand">
          <Link to="/" className="nav-brand">
            <img src="/logo.png" alt="LeafLens AI" className="brand-logo" />
          </Link>
          <p className="footer-tagline">AI-powered plant disease detection for everyone.</p>
        </div>
        <div className="footer-links">
          <Link to="/">Home</Link>
          <Link to="/diagnose">Diagnose</Link>
          <Link to="/about">About</Link>
        </div>
      </div>
      <div className="footer-bottom">
        <p>© 2026 LeafLens AI · Powered by ResNet50 · PlantVillage Dataset · 38 Classes</p>
      </div>
    </footer>
  );
}

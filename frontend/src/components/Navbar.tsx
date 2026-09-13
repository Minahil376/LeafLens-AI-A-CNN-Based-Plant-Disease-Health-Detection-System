import { useEffect, useRef, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';

export default function Navbar() {
  const location = useLocation();
  const [menuOpen, setMenuOpen] = useState(false);
  const navRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const nav = navRef.current;
    if (!nav) return;
    const onScroll = () => {
      nav.classList.toggle('scrolled', window.scrollY > 10);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  const linkClass = (path: string) =>
    `nav-link${location.pathname === path ? ' active' : ''}`;

  return (
    <nav className="navbar" ref={navRef} id="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-brand">
          <img src="/logo.png" alt="LeafLens AI Logo" className="brand-logo" />
        </Link>
        <ul className={`nav-links${menuOpen ? ' open' : ''}`} id="nav-links">
          <li><Link to="/" className={linkClass('/')}>Home</Link></li>
          <li><Link to="/diagnose" className={linkClass('/diagnose')}>Diagnose</Link></li>
          <li><Link to="/about" className={linkClass('/about')}>About</Link></li>
          <li><Link to="/diagnose" className="nav-link nav-cta">Try for Free</Link></li>
        </ul>
        <button
          className={`nav-toggle${menuOpen ? ' open' : ''}`}
          id="nav-toggle"
          aria-label="Toggle menu"
          onClick={() => setMenuOpen(o => !o)}
        >
          <span></span><span></span><span></span>
        </button>
      </div>
    </nav>
  );
}

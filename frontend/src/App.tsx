import { BrowserRouter, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import { Component, ErrorInfo, ReactNode } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import DiagnosePage from './pages/DiagnosePage';
import AboutPage from './pages/AboutPage';

/* ---------- Error Boundary ---------- */
interface EBState { hasError: boolean }
class ErrorBoundary extends Component<{ children: ReactNode }, EBState> {
  state: EBState = { hasError: false };
  static getDerivedStateFromError(): EBState { return { hasError: true }; }
  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error('LeafLens UI error:', error, info);
  }
  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: '4rem', textAlign: 'center' }}>
          <h2>Something went wrong.</h2>
          <p>Please refresh the page to try again.</p>
        </div>
      );
    }
    return this.props.children;
  }
}

/* ---------- Layout ---------- */
function Layout() {
  return (
    <>
      <Navbar />
      <Outlet />
      <Footer />
    </>
  );
}

/* ---------- App ---------- */
export default function App() {
  return (
    <BrowserRouter>
      <ErrorBoundary>
        <Routes>
          <Route element={<Layout />}>
            <Route path="/" element={<HomePage />} />
            <Route path="/diagnose" element={<DiagnosePage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Route>
        </Routes>
      </ErrorBoundary>
    </BrowserRouter>
  );
}

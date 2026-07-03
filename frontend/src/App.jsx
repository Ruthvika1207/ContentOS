import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import ProtectedRoute from "./components/ProtectedRoute";
import Layout from "./components/Layout";

import Auth from "./pages/Auth";
import Dashboard from "./pages/Dashboard";
import BrandBrain from "./pages/BrandBrain";
import ContentStudio from "./pages/ContentStudio";
import CampaignHistory from "./pages/CampaignHistory";
import BrandKnowledge from "./pages/BrandKnowledge";
import CampaignDetails from "./pages/CampaignDetails";

function Analytics() {
  return (
    <h1 className="text-3xl font-bold">
      Analytics (Coming Soon)
    </h1>
  );
}

function Settings() {
  return (
    <h1 className="text-3xl font-bold">
      Settings (Coming Soon)
    </h1>
  );
}

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/auth"
          element={<Auth />}
        />

        <Route
          element={
            <ProtectedRoute>
              <Layout />
            </ProtectedRoute>
          }
        >

          <Route
            path="/"
            element={<Navigate to="/dashboard" replace />}
          />

          <Route
            path="/dashboard"
            element={<Dashboard />}
          />
          <Route
            path="/brand-knowledge"
            element={<BrandKnowledge />}
          />
          <Route
            path="/brand-brain"
            element={<BrandBrain />}
          />

          <Route
            path="/content-studio"
            element={<ContentStudio />}
          />

          <Route
            path="/campaigns"
            element={<CampaignHistory />}
          />

          <Route
            path="/campaign/:id"
            element={<CampaignDetails />}
          />

          <Route
            path="/analytics"
            element={<Analytics />}
          />

          <Route
            path="/settings"
            element={<Settings />}
          />

        </Route>

      </Routes>

    </BrowserRouter>

  );
}

export default App;
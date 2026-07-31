import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {

  const [campaignCount, setCampaignCount] = useState(0);
  const [documentCount, setDocumentCount] = useState(0);

  const userId = localStorage.getItem("user_id");
  const workspaceId = localStorage.getItem("workspace_id");;

  useEffect(() => {

    fetchDashboard();

  }, []);

  const fetchDashboard = async () => {

    try {

      const campaignResponse = await api.get(
        `/campaigns/${userId}`
      );

      setCampaignCount(
        campaignResponse.data.length
      );

      const documentResponse = await api.get(
        `/documents/${workspaceId}`
      );

      setDocumentCount(
        documentResponse.data.length
      );

    } catch (error) {

      console.error(error);

    }

  };

  return (

    <div>

      <h1 className="text-4xl font-bold text-slate-800">

        Welcome back 👋

      </h1>

      <p className="text-gray-500 mt-2">

        Manage your AI-powered marketing campaigns.

      </p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-gray-500">

            Campaigns

          </h2>

          <p className="text-4xl font-bold mt-3">

            {campaignCount}

          </p>

        </div>

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-gray-500">

            Brand Documents

          </h2>

          <p className="text-4xl font-bold mt-3">

            {documentCount}

          </p>

        </div>

        <div className="bg-white rounded-xl shadow p-6">

          <h2 className="text-gray-500">

            AI Agents

          </h2>

          <p className="text-4xl font-bold mt-3">

            7

          </p>

        </div>

      </div>

      <div className="bg-white rounded-xl shadow p-6 mt-8">

        <h2 className="text-2xl font-bold mb-4">

          Quick Actions

        </h2>

        <div className="flex gap-4">

          <button className="bg-indigo-600 text-white px-5 py-3 rounded-lg hover:bg-indigo-700">

            Generate Content

          </button>

          <button className="bg-emerald-600 text-white px-5 py-3 rounded-lg hover:bg-emerald-700">

            Upload Knowledge

          </button>

        </div>

      </div>

    </div>

  );

}

export default Dashboard;
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../services/api";

function CampaignDetails() {

  const { id } = useParams();

  const [campaign, setCampaign] = useState(null);

  useEffect(() => {
    fetchCampaign();
  }, []);

  const fetchCampaign = async () => {

    try {

      const response = await api.get(
        `/campaign/${id}`
      );

      setCampaign(response.data);

    } catch (error) {

      console.error(error);

    }

  };

  if (!campaign) {

    return <p>Loading...</p>;

  }

  return (

    <div className="bg-white rounded-xl shadow-md p-8">

      <h1 className="text-3xl font-bold mb-4">

        {campaign.topic}

      </h1>

      <p className="text-gray-500 mb-8">

        Published:

        {" "}

        {new Date(campaign.created_at).toLocaleString()}

      </p>

      <div className="border rounded-lg p-6 bg-slate-50 whitespace-pre-wrap">

        {campaign.content}

      </div>

    </div>

  );

}

export default CampaignDetails;
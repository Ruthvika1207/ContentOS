import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function CampaignHistory() {

  const [campaigns, setCampaigns] = useState([]);

  const navigate = useNavigate();

  const userId = localStorage.getItem("user_id");

  useEffect(() => {

    fetchCampaigns();

  }, []);

  const fetchCampaigns = async () => {

    try {

      const response = await api.get(
        `/campaigns/${userId}`
      );

      setCampaigns(response.data);

    } catch (error) {

      console.error(error);

    }

  };

  const deleteCampaign = async (id) => {

    try {

      await api.delete(
        `/campaign/${id}`
      );

      fetchCampaigns();

    } catch (error) {

      console.error(error);

    }

  };

  return (

    <div className="bg-white rounded-xl shadow-md p-8">

      <h1 className="text-3xl font-bold mb-8">

        Campaign History

      </h1>

      {

        campaigns.length === 0 ?

        (

          <p className="text-gray-500">

            No campaigns found.

          </p>

        )

        :

        (

          campaigns.map((campaign) => (

            <div

              key={campaign.id}

              className="border rounded-xl p-5 mb-5 flex justify-between items-center"

            >

              <div>

                <h2 className="text-xl font-semibold">

                  {campaign.topic}

                </h2>

                <p className="text-green-600 mt-1">

                  {campaign.status}

                </p>

                <p className="text-gray-500 text-sm mt-1">

                  Published:

                  {" "}

                  {

                    new Date(
                      campaign.created_at
                    ).toLocaleString()

                  }

                </p>

              </div>

              <div className="flex gap-3">

                <button

                  onClick={() =>
                    navigate(
                      `/campaign/${campaign.id}`
                    )
                  }

                  className="bg-indigo-600 text-white px-5 py-2 rounded-lg hover:bg-indigo-700"

                >

                  View

                </button>

                <button

                  onClick={() =>
                    deleteCampaign(
                      campaign.id
                    )
                  }

                  className="bg-red-500 text-white px-5 py-2 rounded-lg hover:bg-red-600"

                >

                  Delete

                </button>

              </div>

            </div>

          ))

        )

      }

    </div>

  );

}

export default CampaignHistory;
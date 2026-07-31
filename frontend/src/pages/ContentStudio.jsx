import { useState } from "react";
import api from "../services/api";

function ContentStudio() {

  const [topic, setTopic] = useState("");

  const [loading, setLoading] =
    useState(false);

  const [research, setResearch] =
    useState("");

  const [strategy, setStrategy] =
    useState("");

  const [content, setContent] =
    useState("");

  const generate = async () => {

  try {

    setLoading(true);

    const workspace_id = localStorage.getItem(
      "workspace_id"
    );

    const response = await api.post(
      "/generate-package",
      {
        workspace_id,
        topic
      }
    );

    setResearch(
      response.data.research
    );

    setStrategy(
      response.data.strategy
    );

    setContent(
      response.data.edited_content
    );

  } catch (error) {

    console.error(error);

    alert("Generation Failed");

  } finally {

    setLoading(false);

  }

};

  return (

    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-2xl font-bold mb-4">
        Content Studio
      </h2>

      <input
        className="w-full border rounded-lg p-3 mb-4"
        placeholder="Research Topic..."
        value={topic}
        onChange={(e) =>
          setTopic(e.target.value)
        }
      />

      <button
        onClick={generate}
        className="w-full bg-indigo-600 text-white py-3 rounded-lg"
      >
        Generate Content Package
      </button>

      {loading && (
        <p className="mt-4">
          Generating...
        </p>
      )}

      {research && (
        <div className="mt-6">
          <h3 className="font-bold text-lg">
            Research Report
          </h3>

          <pre className="whitespace-pre-wrap mt-2">
            {research}
          </pre>
        </div>
      )}

      {strategy && (
        <div className="mt-6">
          <h3 className="font-bold text-lg">
            Strategy Report
          </h3>

          <pre className="whitespace-pre-wrap mt-2">
            {strategy}
          </pre>
        </div>
      )}

      {content && (
        <div className="mt-6">
          <h3 className="font-bold text-lg">
            Content Assets
          </h3>

          <pre className="whitespace-pre-wrap mt-2">
            {content}
          </pre>
        </div>
      )}

    </div>

  );
}

export default ContentStudio;
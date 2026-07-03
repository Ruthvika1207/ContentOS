import { useState } from "react";
import api from "../services/api";

function BrandBrain() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    try {
      const response = await api.post("/chat", {
        workspace_id: "fitness_workspace",
        question,
      });

      setAnswer(response.data.answer);
    } catch (error) {
      setAnswer("Failed to get answer");
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-xl font-bold mb-4">
        Brand Brain
      </h2>

      <input
        className="w-full border rounded-lg p-3"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        onClick={askQuestion}
        className="mt-4 w-full bg-emerald-600 text-white py-3 rounded-lg hover:bg-emerald-700"
      >
        Ask AI
      </button>

      <div className="mt-6 border rounded-lg p-4 min-h-[200px] bg-slate-50">

        <h3 className="font-semibold mb-2">
          AI Response
        </h3>

        <p className="text-gray-700 whitespace-pre-wrap">
          {answer}
        </p>

      </div>

    </div>
  );
}

export default BrandBrain;
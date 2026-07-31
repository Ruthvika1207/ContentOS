import { useState, useEffect } from "react";
import api from "../services/api";

function BrandKnowledge() {

  const [content, setContent] = useState("");
  const [message, setMessage] = useState("");
  const [pdfFile, setPdfFile] = useState(null);
  const [documents, setDocuments] = useState([]);

  const workspaceId = localStorage.getItem("workspace_id");;

  useEffect(() => {
    fetchDocuments();
  }, []);

  const fetchDocuments = async () => {

    try {

      const response = await api.get(
        `/documents/${workspaceId}`
      );

      setDocuments(response.data);

    } catch (error) {

      console.error(error);

    }

  };

  const uploadDocument = async () => {

    try {

      const response = await api.post(
        "/documents",
        {
          workspace_id: workspaceId,
          content
        }
      );

      setMessage(response.data.message);

      setContent("");

      fetchDocuments();

    } catch (error) {

      setMessage("Upload Failed");

    }

  };

  const uploadPdf = async () => {

    if (!pdfFile) {

      alert("Please select a PDF");

      return;

    }

    const formData = new FormData();

    formData.append(
      "workspace_id",
      workspaceId
    );

    formData.append(
      "file",
      pdfFile
    );

    try {

      const response = await api.post(
        "/upload-pdf",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data"
          }
        }
      );

      setMessage(response.data.message);

      setPdfFile(null);

      fetchDocuments();

    } catch (error) {

      console.error(error);

      setMessage("PDF Upload Failed");

    }

  };

  const deleteDocument = async (id) => {

    try {

      await api.delete(
        `/documents/${id}`
      );

      fetchDocuments();

    } catch (error) {

      console.error(error);

    }

  };

  return (

    <div className="bg-white rounded-xl shadow-md p-8">

      <h1 className="text-3xl font-bold mb-6">

        Brand Knowledge

      </h1>

      {/* Upload Text */}

      <textarea

        className="w-full border rounded-lg p-3 h-56"

        placeholder="Paste your brand information..."

        value={content}

        onChange={(e) =>
          setContent(e.target.value)
        }

      />

      <button

        onClick={uploadDocument}

        className="mt-4 bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700"

      >

        Upload Knowledge

      </button>

      {/* Upload PDF */}

      <div className="mt-10">

        <input

          type="file"

          accept=".pdf"

          onChange={(e) =>
            setPdfFile(
              e.target.files[0]
            )
          }

        />

        <button

          onClick={uploadPdf}

          className="mt-4 ml-4 bg-emerald-600 text-white px-6 py-3 rounded-lg hover:bg-emerald-700"

        >

          Upload PDF

        </button>

      </div>

      {/* Status */}

      <p className="mt-6 text-green-600 font-medium">

        {message}

      </p>

      <hr className="my-10" />

      {/* Knowledge Base */}

      <h2 className="text-2xl font-bold mb-6">

        Knowledge Base

      </h2>

      {

        documents.length === 0 ?

        (

          <p className="text-gray-500">

            No documents uploaded yet.

          </p>

        )

        :

        (

          documents.map((doc) => (

            <div

              key={doc.id}

              className="border rounded-xl p-5 mb-4 flex justify-between items-center"

            >

              <div>

                <h3 className="font-semibold text-lg">

                  📄 {doc.filename || "Text Knowledge"}

                </h3>

                <p className="text-gray-500 text-sm mt-1">

                  Uploaded:

                  {" "}

                  {

                    new Date(
                      doc.created_at
                    ).toLocaleDateString()

                  }

                </p>

              </div>

              <button

                onClick={() =>
                  deleteDocument(doc.id)
                }

                className="bg-red-500 text-white px-5 py-2 rounded-lg hover:bg-red-600"

              >

                Delete

              </button>

            </div>

          ))

        )

      }

    </div>

  );

}

export default BrandKnowledge;
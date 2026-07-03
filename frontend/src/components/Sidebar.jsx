import { Link, useNavigate } from "react-router-dom";

function Sidebar() {

  const navigate = useNavigate();

  const logout = () => {

    localStorage.removeItem("token");
    localStorage.removeItem("user_id");

    navigate("/auth");

  };

  return (

    <div className="w-64 bg-white shadow-lg min-h-screen p-6">

      <h1 className="text-3xl font-bold text-indigo-600 mb-8">

        ContentOS

      </h1>

      <nav className="flex flex-col gap-4">

        <Link
          to="/dashboard"
          className="hover:text-indigo-600"
        >
          🏠 Dashboard
        </Link>


        <Link
            to="/brand-knowledge"
            className="hover:text-indigo-600"
        >
            📚 Brand Knowledge
        </Link>

        <Link
          to="/brand-brain"
          className="hover:text-indigo-600"
        >
          🧠 Brand Brain
        </Link>

        <Link
          to="/content-studio"
          className="hover:text-indigo-600"
        >
          ✍️ Content Studio
        </Link>

        <Link
          to="/campaigns"
          className="hover:text-indigo-600"
        >
          📂 Campaign History
        </Link>

        <Link
          to="/analytics"
          className="hover:text-indigo-600"
        >
          📊 Analytics
        </Link>

        <button

          onClick={logout}

          className="mt-10 bg-red-500 text-white py-2 rounded-lg"

        >

          Logout

        </button>

      </nav>

    </div>

  );

}

export default Sidebar;
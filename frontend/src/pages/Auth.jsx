import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Auth() {

  const [isLogin, setIsLogin] = useState(true);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async () => {

    try {

      if (isLogin) {

        const response = await api.post(
          "/login",
          {
            email,
            password
          }
        );

        localStorage.setItem(
          "token",
          response.data.access_token
        );

        localStorage.setItem(
          "user_id",
           response.data.user_id
        );


        navigate("/");

      } else {

        await api.post(
          "/signup",
          {
            email,
            password
          }
        );

        alert(
          "Signup Successful. Please Login."
        );

        setIsLogin(true);

      }

    } catch (error) {

      alert(
        isLogin
          ? "Login Failed"
          : "Signup Failed"
      );

    }

  };

  return (

    <div className="min-h-screen bg-slate-100 flex items-center justify-center">

      <div className="bg-white p-8 rounded-xl shadow-md w-96">

        <h1 className="text-3xl font-bold text-indigo-600 mb-6 text-center">
          ContentOS
        </h1>

        <input
          className="w-full border p-3 rounded mb-4"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <input
          type="password"
          className="w-full border p-3 rounded mb-4"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button
          onClick={handleSubmit}
          className="w-full bg-indigo-600 text-white py-3 rounded"
        >
          {isLogin ? "Login" : "Sign Up"}
        </button>

        <p
          className="text-center mt-4 text-indigo-600 cursor-pointer"
          onClick={() =>
            setIsLogin(!isLogin)
          }
        >
          {isLogin
            ? "Don't have an account? Sign Up"
            : "Already have an account? Login"}
        </p>

      </div>

    </div>

  );
}

export default Auth;
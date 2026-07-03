import Sidebar from "./Sidebar";
import { Outlet } from "react-router-dom";

function Layout() {

  return (

    <div className="flex min-h-screen bg-slate-100">

      <Sidebar />

      <main className="flex-1 p-8">

        <Outlet />

      </main>

    </div>

  );

}

export default Layout;
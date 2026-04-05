import React, { useContext, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import AuthContext from "../context/AuthContext";
import { useGoogleLogin } from "@react-oauth/google";

const Login = () => {
  const hasGoogleClientId = Boolean(import.meta.env.VITE_GOOGLE_CLIENT_ID);
  const [crdentials, setCrdentials] = useState({ username: "", password: "" });

  const { login, googleAuth } = useContext(AuthContext);

  const navigate = useNavigate();

  const handleChange = (e) => {
    setCrdentials({
      ...crdentials,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    console.log("Submitting login...");
    const res = await login(crdentials);

    console.log("Login result:", res);
    if (res) {
      navigate("/dashboard");
    }
  };

  const startGoogleSignin = useGoogleLogin({
    scope: "openid email profile",
    onSuccess: async (tokenResponse) => {
      const res = await googleAuth(tokenResponse.access_token, "access_token");
      if (res) {
        navigate("/dashboard");
      }
    },
    onError: () => console.log("Google signin failed"),
  });

  return (
    <div className="min-h-screen bg-neutral-950 text-white flex items-center justify-center overflow-hidden relative">
      {/* Background Animated Orbs */}
      <div className="absolute -top-37.5 -left-50 w-125 h-125 bg-indigo-500/20 rounded-full blur-[100px] animate-pulse"></div>
      <div
        className="absolute -bottom-50 -right-37.5 w-150 h-150 bg-pink-500/10 rounded-full blur-[100px] animate-pulse"
        style={{ animationDelay: "1s" }}
      ></div>

      <main className="relative z-10 w-full max-w-md mx-auto p-8 sm:p-10 bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl shadow-2xl transition-all duration-700 hover:border-white/20">
        {/* Lock Icon */}
        <div className="flex justify-center mb-6">
          <div className="w-14 h-14 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center shadow-[0_0_20px_rgba(99,102,241,0.15)]">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#a5b4fc"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
          </div>
        </div>

        {/* Heading */}
        <h1 className="text-3xl font-extrabold tracking-tight text-center mb-2 bg-linear-to-br from-white to-indigo-300 bg-clip-text text-transparent">
          Welcome Back
        </h1>
        <p className="text-neutral-400 text-center mb-10 text-sm">
          Sign in to your account to continue
        </p>

        {/* Form */}
        <form className="space-y-6" onSubmit={handleSubmit}>
          {/* Email Field */}
          <div className="space-y-2">
            <label
              htmlFor="email"
              className="block text-sm font-medium text-neutral-300"
            >
              Username
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#71717a"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <rect x="2" y="4" width="20" height="16" rx="2"></rect>
                  <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
                </svg>
              </div>
              <input
                type="text"
                id="username"
                value={crdentials.username}
                onChange={handleChange}
                name="username"
                placeholder="you@example.com"
                className="w-full pl-12 pr-4 py-3.5 bg-white/5 border border-white/10 rounded-xl text-white placeholder-neutral-500 focus:outline-none focus:border-indigo-500/50 focus:ring-2 focus:ring-indigo-500/20 transition-all duration-300"
              />
            </div>
          </div>

          {/* Password Field */}
          <div className="space-y-2">
            <label
              htmlFor="password"
              className="block text-sm font-medium text-neutral-300"
            >
              Password
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#71717a"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <rect
                    x="3"
                    y="11"
                    width="18"
                    height="11"
                    rx="2"
                    ry="2"
                  ></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
              </div>
              <input
                type="password"
                id="password"
                value={crdentials.password}
                onChange={handleChange}
                name="password"
                placeholder="••••••••"
                className="w-full pl-12 pr-4 py-3.5 bg-white/5 border border-white/10 rounded-xl text-white placeholder-neutral-500 focus:outline-none focus:border-indigo-500/50 focus:ring-2 focus:ring-indigo-500/20 transition-all duration-300"
              />
            </div>
          </div>

          {/* Sign In Button */}
          <button
            type="submit"
            className="w-full flex items-center justify-center gap-2 py-3.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl font-semibold transition-all duration-300 shadow-[0_8px_20px_-6px_rgba(99,102,241,0.6)] hover:shadow-[0_12px_25px_-6px_rgba(99,102,241,0.8)] hover:-translate-y-0.5"
          >
            Sign In
            <svg
              width="18"
              height="18"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
          </button>
        </form>

        {/* Divider */}
        <div className="flex items-center gap-4 my-8">
          <div className="flex-1 h-px bg-white/10"></div>
          <span className="text-xs text-neutral-500 uppercase tracking-wider">
            or
          </span>
          <div className="flex-1 h-px bg-white/10"></div>
        </div>

        {hasGoogleClientId ? (
          <div className="mb-6">
            <button
              type="button"
              onClick={() => startGoogleSignin()}
              className="w-full flex items-center justify-center gap-3 py-3.5 bg-white/8 hover:bg-white/14 text-white rounded-xl font-semibold border border-white/15 hover:border-indigo-400/50 transition-all duration-300 shadow-[0_8px_20px_-8px_rgba(0,0,0,0.55)] hover:shadow-[0_10px_24px_-8px_rgba(99,102,241,0.55)] hover:-translate-y-0.5"
            >
              <span className="w-5 h-5 rounded-full bg-white grid place-items-center">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M23.04 12.2615C23.04 11.4451 22.9735 10.8497 22.8296 10.2324H12.2441V14.4148H18.4588C18.3335 15.4546 17.6568 17.0209 16.1534 18.072L16.1323 18.212L19.5439 20.803L19.7803 20.8263C21.9519 18.8719 23.04 15.9946 23.04 12.2615Z" fill="#4285F4"/>
                  <path d="M12.245 23C15.2896 23 17.8445 22.0263 19.7812 20.8264L16.1542 18.0721C15.1838 18.7349 13.8797 19.1972 12.245 19.1972C9.26294 19.1972 6.73304 17.2429 5.81381 14.5417L5.67881 14.553L2.1314 17.2445L2.08496 17.3717C4.01013 21.1545 7.91696 23 12.245 23Z" fill="#34A853"/>
                  <path d="M5.81266 14.5416C5.57085 13.9243 5.43197 13.252 5.43197 12.5576C5.43197 11.8632 5.57085 11.1909 5.80059 10.5736L5.79415 10.4241L2.20221 7.68945L2.08406 7.74344C1.29227 9.28761 0.841797 10.996 0.841797 12.5576C0.841797 14.1192 1.29227 15.8275 2.08406 17.3717L5.81266 14.5416Z" fill="#FBBC05"/>
                  <path d="M12.245 5.91869C14.3065 5.91869 15.7007 6.79389 16.4989 7.52475L19.8574 4.32449C17.8325 2.46995 15.2896 1.11523 12.245 1.11523C7.91696 1.11523 4.01013 2.96059 2.08496 6.74338L5.8015 9.57352C6.73304 6.87239 9.26294 4.91869 12.245 4.91869Z" fill="#EB4335"/>
                </svg>
              </span>
              Continue with Google
            </button>
          </div>
        ) : null}

        {/* Create Account Link */}
        <p className="text-center text-sm text-neutral-400">
          Don't have an account?{" "}
          <Link
            to="/register"
            className="text-indigo-400 hover:text-indigo-300 font-semibold transition-colors duration-200"
          >
            Create one
          </Link>
        </p>
      </main>
    </div>
  );
};

export default Login;

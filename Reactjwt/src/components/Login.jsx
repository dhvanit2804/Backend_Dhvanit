import React, { useContext, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import AuthContext from '../context/AuthContext';

const Login = () => {

    const [crdentials, setCrdentials] = useState({ username: "", password: "" })

    const { login } = useContext(AuthContext)

    const navigate = useNavigate()

    const handleChange = (e) => {
        setCrdentials({
            ...crdentials,
            [e.target.name]: e.target.value
        })
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        console.log("Submitting login...");
        const res = await login(crdentials);

        console.log("Login result:", res);

        navigate("/dashboard");
    };

    return (
        <div className="min-h-screen bg-neutral-950 text-white flex items-center justify-center overflow-hidden relative">
            {/* Background Animated Orbs */}
            <div className="absolute top-[-150px] left-[-200px] w-[500px] h-[500px] bg-indigo-500/20 rounded-full blur-[100px] animate-pulse"></div>
            <div className="absolute bottom-[-200px] right-[-150px] w-[600px] h-[600px] bg-pink-500/10 rounded-full blur-[100px] animate-pulse" style={{ animationDelay: '1s' }}></div>

            <main className="relative z-10 w-full max-w-md mx-auto p-8 sm:p-10 bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl shadow-2xl transition-all duration-700 hover:border-white/20">
                {/* Lock Icon */}
                <div className="flex justify-center mb-6">
                    <div className="w-14 h-14 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center shadow-[0_0_20px_rgba(99,102,241,0.15)]">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#a5b4fc" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                        </svg>
                    </div>
                </div>

                {/* Heading */}
                <h1 className="text-3xl font-extrabold tracking-tight text-center mb-2 bg-gradient-to-br from-white to-indigo-300 bg-clip-text text-transparent">
                    Welcome Back
                </h1>
                <p className="text-neutral-400 text-center mb-10 text-sm">
                    Sign in to your account to continue
                </p>

                {/* Form */}
                <form className="space-y-6" onSubmit={handleSubmit}>
                    {/* Email Field */}
                    <div className="space-y-2">
                        <label htmlFor="email" className="block text-sm font-medium text-neutral-300">
                            Username
                        </label>
                        <div className="relative">
                            <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#71717a" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                    <rect x="2" y="4" width="20" height="16" rx="2"></rect>
                                    <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
                                </svg>
                            </div>
                            <input
                                type="text"
                                id="username"
                                value={crdentials.username}
                                onChange={handleChange}
                                name='username'
                                placeholder="you@example.com"
                                className="w-full pl-12 pr-4 py-3.5 bg-white/5 border border-white/10 rounded-xl text-white placeholder-neutral-500 focus:outline-none focus:border-indigo-500/50 focus:ring-2 focus:ring-indigo-500/20 transition-all duration-300"
                            />
                        </div>
                    </div>

                    {/* Password Field */}
                    <div className="space-y-2">
                        <label htmlFor="password" className="block text-sm font-medium text-neutral-300">
                            Password
                        </label>
                        <div className="relative">
                            <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#71717a" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                                </svg>
                            </div>
                            <input
                                type="password"
                                id="password"
                                value={crdentials.password}
                                onChange={handleChange}
                                name='password'
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
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </button>
                </form>

                {/* Divider */}
                <div className="flex items-center gap-4 my-8">
                    <div className="flex-1 h-px bg-white/10"></div>
                    <span className="text-xs text-neutral-500 uppercase tracking-wider">or</span>
                    <div className="flex-1 h-px bg-white/10"></div>
                </div>

                {/* Create Account Link */}
                <p className="text-center text-sm text-neutral-400">
                    Don't have an account?{' '}
                    <Link to="/register" className="text-indigo-400 hover:text-indigo-300 font-semibold transition-colors duration-200">
                        Create one
                    </Link>
                </p>
            </main>
        </div>
    );
};

export default Login;

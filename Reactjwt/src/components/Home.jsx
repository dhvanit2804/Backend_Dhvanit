import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Home = () => {

    return (
        <div className="min-h-screen bg-neutral-950 text-white flex items-center justify-center overflow-hidden relative">
            {/* Background Animated Orbs */}
            <div className="absolute top-[-150px] left-[-200px] w-[500px] h-[500px] bg-indigo-500/20 rounded-full blur-[100px] animate-pulse"></div>
            <div className="absolute bottom-[-200px] right-[-150px] w-[600px] h-[600px] bg-pink-500/10 rounded-full blur-[100px] animate-pulse" style={{ animationDelay: '1s' }}></div>

            <main className="relative z-10 w-full max-w-2xl mx-auto p-8 sm:p-12 bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl text-center shadow-2xl transition-all duration-700 hover:border-white/20">
                <span className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-500/10 text-indigo-300 rounded-full text-sm font-semibold tracking-wider uppercase mb-8 border border-indigo-500/20 shadow-[0_0_15px_rgba(99,102,241,0.1)]">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                        <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                        <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                    </svg>
                    Security First
                </span>

                <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight mb-6 bg-gradient-to-br from-white to-indigo-300 bg-clip-text text-transparent">
                    Platform Access
                </h1>

                <p className="text-lg text-neutral-400 mb-12 max-w-md mx-auto leading-relaxed">
                    Experience seamless authentication powered by Django REST framework and React.
                    Secure, fast, and beautifully designed.
                </p>

                <div className="flex flex-col sm:flex-row gap-5 justify-center items-center">

                    <Link to="/login"
                        className="flex items-center justify-center gap-2 w-full sm:w-auto px-8 py-4 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl font-semibold transition-all duration-300 shadow-[0_8px_20px_-6px_rgba(99,102,241,0.6)] hover:shadow-[0_12px_25px_-6px_rgba(99,102,241,0.8)] hover:-translate-y-1"
                    >
                        Sign In
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
                            <polyline points="10 17 15 12 10 7"></polyline>
                            <line x1="15" y1="12" x2="3" y2="12"></line>
                        </svg>
                    </Link>
                    <Link to="/register" className="flex items-center justify-center gap-2 w-full sm:w-auto px-8 py-4 bg-transparent hover:bg-white/5 border border-white/10 hover:border-white/20 text-white rounded-xl font-semibold transition-all duration-300 hover:-translate-y-1">
                        Create Account
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                            <circle cx="9" cy="7" r="4"></circle>
                            <line x1="19" y1="8" x2="19" y2="14"></line>
                            <line x1="22" y1="11" x2="16" y2="11"></line>
                        </svg>
                    </Link>
                </div>
            </main>
        </div>
    );
};

export default Home;
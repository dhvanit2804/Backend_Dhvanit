import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import AuthContext from '../context/AuthContext';

const Dashboard = () => {

    const { logout } = useContext(AuthContext)

    return (
        <div className="min-h-screen bg-neutral-950 text-white overflow-hidden relative font-sans">
            {/* Background Animated Orbs */}
            <div className="absolute top-[-150px] left-[-200px] w-[500px] h-[500px] bg-indigo-500/20 rounded-full blur-[100px] animate-pulse"></div>
            <div className="absolute bottom-[-200px] right-[-150px] w-[600px] h-[600px] bg-pink-500/10 rounded-full blur-[100px] animate-pulse" style={{ animationDelay: '1s' }}></div>

            {/* Simple Top Navigation */}
            <nav className="relative z-20 border-b border-white/10 bg-white/5 backdrop-blur-xl">
                <div className="max-w-7xl mx-auto px-6">
                    <div className="flex items-center justify-between h-24">
                        {/* Logo / Brand */}
                        <div className="flex items-center gap-3">
                            <div className="w-12 h-12 rounded-xl bg-indigo-500/20 border border-indigo-500/30 flex items-center justify-center shadow-lg shadow-indigo-500/10">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#a5b4fc" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                                </svg>
                            </div>
                            <span className="font-extrabold text-3xl tracking-tight bg-gradient-to-r from-white to-indigo-300 bg-clip-text text-transparent">
                                SecureApp
                            </span>
                        </div>

                        {/* Actions */}
                        <div className="flex items-center">
                            <button
                                onClick={logout}
                                className="flex items-center justify-center gap-2 px-6 py-3 bg-white/5 hover:bg-white/10 border border-white/10 hover:border-white/20 text-white rounded-xl font-medium transition-all duration-300"
                            >
                                Log out
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                    <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                                    <polyline points="16 17 21 12 16 7"></polyline>
                                    <line x1="21" y1="12" x2="9" y2="12"></line>
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
            </nav>

            {/* Main Welcome Message */}
            <main className="relative z-10 flex flex-col items-center justify-center" style={{ minHeight: 'calc(100vh - 96px)' }}>
                <div className="text-center p-12 bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl shadow-2xl max-w-3xl w-full mx-4 transform hover:scale-[1.01] transition-transform duration-500">
                    <div className="w-24 h-24 bg-indigo-600 rounded-full flex items-center justify-center mx-auto mb-8 text-4xl font-bold shadow-xl shadow-indigo-500/30 ring-4 ring-indigo-500/20">
                        U
                    </div>
                    <h1 className="text-5xl sm:text-6xl font-extrabold text-white mb-6 tracking-tight">
                        Welcome, User!
                    </h1>
                    <p className="text-xl sm:text-2xl text-neutral-400 font-light">
                        You have successfully authenticated.
                    </p>
                </div>
            </main>
        </div>
    );
};

export default Dashboard;

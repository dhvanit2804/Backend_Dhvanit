import React, { createContext, useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
      fetchUserData(token);
    } else {
      setLoading(false);
    }
  }, []);

  const fetchUserData = async (token) => {
    try {
      const response = await axios.get("http://localhost:8000/api/dashboard/");
      setUser(response.data.user);
      return response.data.user;
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  const login = async (crdentials) => {
    try {
      const response = await axios.post(
        "http://localhost:8000/api/auth/login/",
        crdentials
      );

      const { access, refresh } = response.data;

      localStorage.setItem("token", access);
      localStorage.setItem("refreshToken", refresh);

      axios.defaults.headers.common["Authorization"] = `Bearer ${access}`;

      setUser({ username: crdentials.username });
      return true;

    } catch (error) {
      console.log(error);
      return false;
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("refreshToken");
    delete axios.defaults.headers.common["Authorization"];
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{ user, loading, login, logout, fetchUserData }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;

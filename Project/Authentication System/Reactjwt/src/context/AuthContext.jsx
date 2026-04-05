import React, { createContext, useEffect, useState } from "react";
import axios from "axios";

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
      localStorage.removeItem("token");
      localStorage.removeItem("refreshToken");
      delete axios.defaults.headers.common["Authorization"];
      setUser(null);
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

  const googleAuth = async (token, tokenType = "id_token") => {
    try {
      const payload = tokenType === "access_token"
        ? { access_token: token }
        : { id_token: token };

      const response = await axios.post("http://localhost:8000/api/auth/google/", {
        ...payload,
      });

      const { access, refresh, user: loggedInUser } = response.data;

      localStorage.setItem("token", access);
      localStorage.setItem("refreshToken", refresh);
      axios.defaults.headers.common["Authorization"] = `Bearer ${access}`;
      setUser(loggedInUser);
      return true;
    } catch (error) {
      console.log(error);
      return false;
    } finally {
      setLoading(false);
    }
  };

  const register = async (crdentials) => {
    try {
      const response = await axios.post("http://localhost:8000/api/auth/register/", crdentials)
      console.log(response.data)
      return true;
    } catch (error) {
      console.log(error);
      return false;
    }
  }

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("refreshToken");
    delete axios.defaults.headers.common["Authorization"];
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{ user, loading, login, logout, register, fetchUserData, googleAuth }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;

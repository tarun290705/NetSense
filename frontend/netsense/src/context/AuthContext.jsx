import { createContext, useContext, useState } from "react";

/**
 * AuthContext is used to manage user authentication state
 * (login, logout, user info)
 */
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);       // user info
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Fake login (for now – replace with backend later)
  const login = (username) => {
    setUser({ username });
    setIsAuthenticated(true);
  };

  const logout = () => {
    setUser(null);
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated,
        login,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook (clean usage in components)
export const useAuth = () => {
  return useContext(AuthContext);
};

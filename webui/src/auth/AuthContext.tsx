import { createContext, useContext, useState } from "react";

type User = {
  token: string;
  role: "admin" | "developer";
};

type AuthContextType = {
  user: User | null;
  login: (u: User) => void;
  logout: () => void;
};

const AuthContext = createContext<AuthContextType>({
  user: null,
  login: () => {},
  logout: () => {},
});

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(() => {
    const raw = localStorage.getItem("auth");
    return raw ? JSON.parse(raw) : null;
  });

  const login = (u: User) => {
    setUser(u);
    localStorage.setItem("auth", JSON.stringify(u));
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("auth");
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);

export default function Navbar() {
  return (
    <div style={styles.nav}>
      <h2 style={styles.title}>
        NetSense
      </h2>
    </div>
  );
}

const styles = {
  nav: {
    background: "#2563eb",
    padding: "18px 30px",
    display: "flex",
    justifyContent: "center", // 👈 CENTERED
    alignItems: "center",
    color: "#ffffff",
    boxShadow: "0 6px 18px rgba(0,0,0,0.25)",
  },

  title: {
    fontSize: "22px",
    fontWeight: "600",
    letterSpacing: "0.4px",
  },
};


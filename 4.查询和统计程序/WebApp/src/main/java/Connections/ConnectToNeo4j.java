package Connections;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectToNeo4j {

    private static final String URL = "jdbc:neo4j://localhost:7474/";

    private static final String name = "neo4j";
    private static final String pwd = "1";

    private static Connection connection;

    public static Connection getConnection() throws SQLException {
        if (connection == null){
            connection = DriverManager.getConnection(URL, name, pwd);
        }
        return connection;
    }

}

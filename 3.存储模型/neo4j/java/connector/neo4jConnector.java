package connector;

import org.neo4j.driver.v1.AuthTokens;
import org.neo4j.driver.v1.Driver;
import org.neo4j.driver.v1.GraphDatabase;

public class neo4jConnector {
    private static final String URL = "bolt://localhost:7687";

    private static final String name = "neo4j";
    private static final String pwd = "1";

    private static Driver driver;

    public static Driver getDriver(){
        if (driver == null){
            Driver driver = GraphDatabase.driver(URL,AuthTokens.basic(name,pwd));
            return driver;
        }else {
            return driver;
        }
    }
}

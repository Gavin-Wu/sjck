package test;

import service.neo4jService;

public class test {
    public static void main(String[] args){
        neo4jService neo4jService = new neo4jService();
        neo4jService.getMovieByDirector("Ray Etheridge");
    }
}

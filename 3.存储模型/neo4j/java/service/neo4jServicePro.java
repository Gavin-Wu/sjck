package service;

import connector.neo4jConnector;
import org.neo4j.driver.v1.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.Timer;

import static org.neo4j.driver.v1.Values.parameters;

public class neo4jServicePro {
    Driver driver = neo4jConnector.getDriver();

    /**
     * 1输入导演名字，返回导演指导过的电影数目
     * @param name 导演名字
     * @return 电影数量
     */

    public Integer getMovieByDirector(String name){
        ArrayList movies = new ArrayList();
        ArrayList rates = new ArrayList();

        try(Session session = driver.session()) {
            Long d1 = new Date().getTime();
            StatementResult result = session.run("Match (n:Director)-[]-(m:Movie) where n.name= $name return m"
                    , parameters("name",name));
            int i = 0;
            while(result.hasNext()){
                Value movie = result.next().get(0);
                movies.add(movie.get("name"));
                rates.add(movie.get("rate"));
                i++;
            }
//            System.out.println(movies);
//            System.out.println(imdbs);
            Long d2 = new Date().getTime();
            System.out.println(d2-d1);
            return i;
        }
    }

    /**
     * 2输入演员名字，返回演员演过的电影数目
     * @param name 演员名字
     * @return 电影数量
     */

    public Integer getMovieByActor(String name){
        ArrayList movies = new ArrayList();
        ArrayList rates = new ArrayList();

        try(Session session = driver.session()) {
            StatementResult result = session.run("Match (n:Actor)-[]-(m:Movie) where n.name= $name return m"
                    , parameters("name",name));
            int i = 0;
            while(result.hasNext()){
                Value movie = result.next().get(0);
                movies.add(movie.get("name"));
                rates.add(movie.get("rate"));
                i++;
            }
//            System.out.println(movies);
//            System.out.println(imdbs);
            return i;
        }
    }

    /**
     * 3输入类型名称，返回该类型包括的电影数目
     * @param name 类型名称
     * @return 电影数量
     */

    public Integer getMovieByGenre(String name){
        ArrayList movies = new ArrayList();
        ArrayList rates = new ArrayList();

        try(Session session = driver.session()) {
            StatementResult result = session.run("Match (n:Genre)-[]-(m:Movie) where n.name= $name return m"
                    , parameters("name",name));
            int i = 0;
            while(result.hasNext()){
                Value movie = result.next().get(0);
                movies.add(movie.get("name"));
                rates.add(movie.get("rate"));
                i++;
            }
//            System.out.println(movies);
//            System.out.println(rates);
            return i;
        }
    }

    /**
     * 4输入语言名称，返回该语言的电影数目
     * @param name 语言名称
     * @return 电影数量
     */

    public Integer getMovieByLanguage(String name){
        ArrayList movies = new ArrayList();
        ArrayList rates = new ArrayList();

        try(Session session = driver.session()) {
            StatementResult result = session.run("Match (n:Language)-[]-(m:Movie) where n.name= $name return m"
                    , parameters("name",name));
            int i = 0;
            while(result.hasNext()){
                Value movie = result.next().get(0);
                movies.add(movie.get("name"));
                rates.add(movie.get("rate"));
                i++;
            }
//            System.out.println(movies);
//            System.out.println(rates);
            return i;
        }
    }

    /**
     * 5输入工作室名称，返回该工作室的电影数目
     * @param name 工作室名称
     * @return 电影数量
     */

    public Integer getMovieByStudio(String name){
        ArrayList movies = new ArrayList();
        ArrayList rates = new ArrayList();

        try(Session session = driver.session()) {
            StatementResult result = session.run("Match (n:Studio)-[]-(m:Movie) where n.name= $name return m"
                    , parameters("name",name));
            int i = 0;
            while(result.hasNext()){
                Value movie = result.next().get(0);
                movies.add(movie.get("name"));
                rates.add(movie.get("rate"));
                i++;
            }
//            System.out.println(movies);
//            System.out.println(rates);
            return i;
        }
    }

    /**
     * 6输入类型和演员名称，返回合作数目
     * @param name1,name2 类型名称 演员名称
     * @return 合作数目
     */

    public Integer getActorByGenre(String name1,String name2){
        Integer num = 0;
        try(Session session = driver.session()) {
            StatementResult result = session.run("match (g:Genre)-[]-(m:Movie)-[]-(a:Actor) where g.name=$name1 and a.name=$name2 return count(m)"
                    , parameters("name1",name1,"name2",name2));
            while(result.hasNext()){
//                System.out.println(result.next().fields().get(0));
                num = result.next().fields().get(0).value().asInt();
            }
        }
        return num;
    }

    /**
     * 7输入类型和导演名称，返回合作数目
     * @param name1,name2 类型名称 导演名称
     * @return 合作数目
     */

    public Integer getDirectorByGenre(String name1,String name2){
        Integer num = 0;
        try(Session session = driver.session()) {
            StatementResult result = session.run("match (g:Genre)-[]-(m:Movie)-[]-(d:Director) where g.name=$name1 and d.name=$name2 return count(m)"
                    , parameters("name1",name1,"name2",name2));
            while(result.hasNext()){
//                System.out.println(result.next().fields().get(0));
                num = result.next().fields().get(0).value().asInt();
            }
        }
        return num;
    }

    /**
     * 8输入导演和演员，返回合作数目
     * @param name1,name2 导演名称 演员名称
     * @return 合作数目
     */

    public Integer getDirectorByActor(String name1,String name2){
        Integer num = 0;
        try(Session session = driver.session()) {
            StatementResult result = session.run("match (d:Director)-[]-(m:Movie)-[]-(a:Actor) where d.name=$name1 and a.name=$name2 return count(m)"
                    , parameters("name1",name1,"name2",name2));
            while(result.hasNext()){
//                System.out.println(result.next().fields().get(0));
                num = result.next().fields().get(0).value().asInt();
            }
        }
        return num;
    }


    /**
     * 9输入时间范围，返回电影数目
     * @param time1 time2 时间范围
     * @return 电影数目
     */

    public Integer getDirectorByGenre(Timer time1, Timer time2){
        ArrayList movies = new ArrayList();

        try(Session session = driver.session()) {
            StatementResult result = session.run("match (n:Movie) where n.time>= $time1 and n.time<= $time2 return n"
                    , parameters("time1",time1,"time2",time2));
            int i = 0;
            while(result.hasNext()){
                Value movie = result.next().get(0);
                movies.add(movie.get("name"));
                i++;
            }
//            System.out.println(movies);
            return i;
        }
    }

    /**
     * 10输入电影名称，返回版本数目
     * @param name 电影名称
     * @return 版本数目
     */

    public Integer getMovieVersion(String name){
        Integer num = 0;
        try(Session session = driver.session()) {
            StatementResult result = session.run("Match (n:Movie) where n.name =~$name return count(n)"
                    , parameters("name",name));
            while(result.hasNext()){
                num = result.next().fields().get(0).value().asInt();
            }
            return num;
        }
    }
}

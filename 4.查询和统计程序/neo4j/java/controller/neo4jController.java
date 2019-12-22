package controller;
import org.springframework.stereotype.Controller;
import service.neo4jService;
import org.springframework.web.bind.annotation.*;

@Controller
public class neo4jController {
    neo4jService neo4jService = new neo4jService();

    @RequestMapping(value = "/api/test" , method = RequestMethod.GET ,produces = "application/json")
    public Integer getData(@RequestParam("name") String name) {
        Integer result = neo4jService.getMovieByActor(name);
        return result;
    }
}

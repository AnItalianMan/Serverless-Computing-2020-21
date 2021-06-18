package com.serverlessproject.logconsumer.controller;


import com.serverlessproject.logconsumer.service.LogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class LoggerController {

    @Autowired
    private LogService logService;

    @GetMapping(value = "/getlogs")
    @CrossOrigin
    public List<String> getLogs() throws InterruptedException {
        Thread.sleep(3000);
        return logService.getLogs();
    }
}

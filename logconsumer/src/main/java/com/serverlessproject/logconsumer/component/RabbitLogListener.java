package com.serverlessproject.logconsumer.component;

import com.serverlessproject.logconsumer.service.LogService;
import org.springframework.amqp.rabbit.annotation.RabbitListener;

public class RabbitLogListener {

    private final LogService logService;


    public RabbitLogListener(LogService logService) {
        this.logService = logService;
    }

    @RabbitListener(queues = "#{rabbitConfiguration.getQueueName()}")
    private void logListener(String log) {
        logService.saveLog(log);
    }


}

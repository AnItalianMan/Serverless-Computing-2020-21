package com.serverlessproject.logconsumer.component;

import com.serverlessproject.logconsumer.service.SaveLogService;
import org.springframework.amqp.rabbit.annotation.RabbitListener;

public class RabbitLogListener {

    private final SaveLogService saveLogService;

    public RabbitLogListener(SaveLogService saveLogService) {
        this.saveLogService = saveLogService;
    }

    @RabbitListener(queues = "${rabbit.queue.name}")
    private void logListener(String log) {
        saveLogService.saveLog(log);
    }


}

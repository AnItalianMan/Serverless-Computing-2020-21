package com.serverlessproject.logconsumer.service;

import java.util.List;

public interface LogService {

    void saveLog(String log);

    List<String> getLogs();
}

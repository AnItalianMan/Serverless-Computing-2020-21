package com.serverlessproject.logconsumer.dao;

import java.util.List;

public interface LoggerDao {
    void savelog(String log);

    List<String> retreiveLogs();
}

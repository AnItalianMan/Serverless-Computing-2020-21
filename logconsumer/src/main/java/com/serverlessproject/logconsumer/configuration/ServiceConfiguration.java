package com.serverlessproject.logconsumer.configuration;


import com.serverlessproject.logconsumer.service.SaveLogService;
import com.serverlessproject.logconsumer.service.SaveLogServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ServiceConfiguration {

    @Autowired
    private DaoConfiguration daoConfiguration;

    @Bean
    public SaveLogService saveLogService(){
        return new SaveLogServiceImpl(daoConfiguration.loggerDao());
    }
}

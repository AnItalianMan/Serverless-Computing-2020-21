package com.serverlessproject.logconsumer.configuration;

import com.serverlessproject.logconsumer.component.RabbitLogListener;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.amqp.core.Queue;

@Configuration
public class RabbitConfiguration {

    @Value("#{environment.RABBIT_USER_USERNAME}")
    private String username;

    @Value("#{environment.RABBIT_USER_PASSWORD}")
    private String password;

    @Value("#{environment.RABBIT_QUEUE_NAME}")
    private String queueName;

    @Value("#{environment.RABBIT_HOST}")
    private String hostname;

    @Autowired
    private ServiceConfiguration serviceConfiguration;

    @Bean
    public RabbitLogListener rabbitLogListener(){
        return new RabbitLogListener(serviceConfiguration.logService());
    }

    public String getQueueName() {
        return String.valueOf(queueName);
    }

    @Bean
    public ConnectionFactory pooledConnectionFactory() {
        CachingConnectionFactory cachingConnectionFactory = new CachingConnectionFactory(hostname);
        cachingConnectionFactory.setUsername(username);
        cachingConnectionFactory.setPassword(password);
        return cachingConnectionFactory;
    }

    @Bean
    public Queue queue(){
        return new Queue(getQueueName(), false);
    }


}

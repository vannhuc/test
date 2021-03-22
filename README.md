package com.fjs.webupload;

import org.apache.http.HttpHost;
import org.apache.http.impl.client.*;
import org.apache.http.impl.conn.DefaultProxyRoutePlanner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntity;
import org.apache.http.entity.mime.content.InputStreamBody;
import org.apache.http.util.EntityUtils;

import javax.net.ssl.SSLContext;
import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;
import org.apache.http.conn.ssl.TrustStrategy;
import org.apache.http.ssl.SSLContextBuilder;
import java.security.KeyStoreException;
import java.net.HttpURLConnection;

@SpringBootApplication
public class WebuploadApplication {

    public static void main(String[] args) throws IOException, NoSuchAlgorithmException, KeyStoreException, KeyManagementException {
        SpringApplication.run(WebuploadApplication.class, args);
        uploadFile();
    }


    private static void uploadFile() throws IOException, KeyManagementException, KeyStoreException, NoSuchAlgorithmException {

        SSLContext trustAllCertSSLContext = new SSLContextBuilder().loadTrustMaterial(null, (TrustStrategy) (x509Certificates, s) -> true).build();

        File inFile = new File("C:\\Users\\nhuc-tv\\Desktop\\Desktop.zip");
        HttpPost httppost = new HttpPost("http://localhost:8080/upload");

        //proxy
        //////////////////////////////////////
        //no authe
        HttpHost proxy = new HttpHost("127.0.0.1", 809);
        DefaultProxyRoutePlanner routePlanner = new DefaultProxyRoutePlanner(proxy);
        CloseableHttpClient httpClient=HttpClientBuilder.create().setSSLContext(trustAllCertSSLContext).setRoutePlanner(routePlanner).build();

        //authe
        final String username="nhuc123";
        final String password="Ntk123451";

        //CredentialsProvider credsProvider = new BasicCredentialsProvider();
        //credsProvider.setCredentials( new AuthScope("127.0.0.1", 809), new UsernamePasswordCredentials(username, password) );
        //HttpClientBuilder clientBuilder = HttpClientBuilder.create();
        //
        //clientBuilder.useSystemProperties();
        //clientBuilder.setProxy(new HttpHost("127.0.0.1", 809));
        //clientBuilder.setDefaultCredentialsProvider(credsProvider);
        //clientBuilder.setProxyAuthenticationStrategy(new ProxyAuthenticationStrategy());
        //
        //CloseableHttpClient httpClient = clientBuilder.build();




        //////////////////////////////////////

        FileInputStream fis =  new FileInputStream(inFile);
        MultipartEntity entity = new MultipartEntity();
        entity.addPart("file", new InputStreamBody(fis, inFile.getName()));
        httppost.setEntity(entity);

        // execute the request
        HttpResponse response = httpClient.execute(httppost);

        int statusCode = response.getStatusLine().getStatusCode();
        HttpEntity responseEntity = response.getEntity();
        String responseString = EntityUtils.toString(responseEntity, "UTF-8");

        if (statusCode == HttpURLConnection.HTTP_OK) {
            System.err.println("StatusCode : [" + statusCode + "] " + responseString);
        } else {
            System.err.println("異常終了しました - StatusCode : [" + statusCode + "] " + responseString);
        }
    }
}


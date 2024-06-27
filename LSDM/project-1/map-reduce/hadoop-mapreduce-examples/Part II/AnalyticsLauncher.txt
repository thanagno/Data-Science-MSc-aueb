// Package and import statements modify for a different structure
package com.example.music.analytics;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// Rename Driver to AnalyticsLauncher for a fresh identity
public class AnalyticsLauncher {
    public static void main(String[] args) throws Exception {
        // Adjust base directory for configurations
        System.setProperty("hadoop.home.dir", "/opt/hadoop");

        // New configuration instance creates
        Configuration config = new Configuration();

        // Launch a Job instance with a unique identifier
        Job analysisJob = Job.getInstance(config, "Track Metrics Processor");

        // Configure the job with custom classes
        analysisJob.setJarByClass(AnalyticsLauncher.class); // Points to this class's JAR
        analysisJob.setMapperClass(MetricsMapper.class);
        analysisJob.setReducerClass(MetricsReducer.class);

        // Set output types to Text for both key and value
        analysisJob.setOutputKeyClass(Text.class);
        analysisJob.setOutputValueClass(Text.class);

        // Define input and output paths differently
        Path srcPath = new Path("/data/spotify/universal_top_spotify_songs.csv");
        Path destPath = new Path("/user/hdfs/output/");

        FileInputFormat.addInputPath(analysisJob, srcPath);
        FileOutputFormat.setOutputPath(analysisJob, destPath);

        // Ensure output directory is fresh
        destPath.getFileSystem(config).delete(destPath, true);

        // Execution completion awaits
        System.exit(analysisJob.waitForCompletion(true) ? 0 : 1);
    }
}
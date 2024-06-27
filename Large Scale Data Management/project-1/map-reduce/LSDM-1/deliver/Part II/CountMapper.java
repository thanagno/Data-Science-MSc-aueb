package org.example;
// package gr.aueb.panagiotisl.mapreduce.wordcount;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class CountMapper extends Mapper<LongWritable, Text, Text, Text> {

    @Override
    protected void map(LongWritable recordKey, Text recordValue, Context outputContext) throws IOException, InterruptedException {
        if (recordKey.get() == 0 && recordValue.toString().startsWith("spotify_id")) {
            return; // Skip header row
        }

        String[] dataFields = recordValue.toString().split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);

        if (dataFields.length > 13) {
            String region = dataFields[6].trim().replace("\"", "");
            String date = dataFields[7].trim().replace("\"", "");
            String ScoreRythm = dataFields[13].trim().replace("\"", "");
            String trackName = dataFields[1];

            if (region.isEmpty() || date.isEmpty() || ScoreRythm.equals("0") || trackName.isEmpty()) {
                return;
            }

            String period = date.substring(0, 7); // YYYY-MM
            Text compositeKey = new Text(region + ":" + period);
            Text compositeValue = new Text(trackName + "|||" + ScoreRythm);

            outputContext.write(compositeKey, compositeValue);
        }
    }
}
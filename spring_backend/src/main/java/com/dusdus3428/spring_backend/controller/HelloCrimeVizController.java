package com.dusdus3428.spring_backend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloCrimeVizController {
	@GetMapping("/hello")
	public String hello() {
		return "Hello, CrimeViz!";
	}
}

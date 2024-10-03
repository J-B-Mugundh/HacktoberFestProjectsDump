'use client'

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Github, Linkedin, Mail } from "lucide-react"
import { Switch } from "@/components/ui/switch"




export function PortfolioJs() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      {/* Header */}
      <header className="p-4 border-b">
        <nav className="container mx-auto flex justify-between items-center">
          <div className="flex items-center space-x-4">
            <Avatar>
              <AvatarImage src="https://github.com/Aditxgupta/multiverse/blob/main/aaas.jpg?raw=true" alt="Aditya Gupta" />
              <AvatarFallback>AG</AvatarFallback>
            </Avatar>
            <h1 className="text-2xl font-bold">Aditya Gupta</h1>
            <Switch />

          </div>
          <div className="space-x-4">
            <Button variant="ghost">About</Button>  
            <Button variant="ghost">Projects</Button>
            <Button variant="ghost">Contact</Button>
          </div>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="py-20 text-center">
        <div className="container mx-auto">
          <h2 className="text-4xl font-bold mb-4">Welcome to My Portfolio  </h2>
          <p className="text-xl mb-8">I'm a developer passionate about creating amazing Products.</p>
          <Button>View My Work</Button>
        </div>
      </section>

      {/* Projects Section */}
      <section className="py-20 bg-muted">
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold mb-8 text-center">Projects</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[1, 2, 3].map((project) => (
                <Card key={project}>
                  <CardHeader>
                    <CardTitle>Project {project}</CardTitle>
                    <CardDescription>A short description of the project</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <p>This is a brief overview of what the project entails and the technologies.</p>
                  </CardContent>
                  <CardFooter>
                    <Button variant="outline">View Project</Button>
                  </CardFooter>
                </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="py-20">
        <div className="container mx-auto max-w-2xl">
          <h2 className="text-3xl font-bold mb-8 text-center">Get in Touch</h2>
          <Card>
            <CardHeader>
              <CardTitle>Contact Me</CardTitle>
              <CardDescription>Fill out the form below to send me a message.</CardDescription>
            </CardHeader>
            <CardContent>
              <form className="space-y-4">
                <Input placeholder="Your Name" />
                <Input type="email" placeholder="Your Email" />
                <Textarea placeholder="Your Message" />
                <Button type="submit" className="w-full">Send Message</Button>
              </form>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-6 border-t">
        <div className="container mx-auto flex justify-center space-x-4">
          <Button variant="ghost" size="icon">
            <Github className="h-5 w-5" />
            <span className="sr-only">GitHub</span>
          </Button>
          <Button variant="ghost" size="icon">
            <Linkedin className="h-5 w-5" />
            <span className="sr-only">LinkedIn</span>
          </Button>
          <Button variant="ghost" size="icon">
            <Mail className="h-5 w-5" />
            <span className="sr-only">Email</span>
          </Button>
        </div>
      </footer>
    </div>
  ) 
}